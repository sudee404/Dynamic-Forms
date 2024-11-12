# models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid

User = get_user_model()

class Form(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='forms')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + '-' + str(uuid.uuid4())[:6]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    QUESTION_TYPES = (
        ('text', 'Text'),
        ('number', 'Number'),
        ('choice', 'Multiple Choice'),
    )
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    choices = models.TextField(blank=True, help_text="Comma-separated values for multiple choice questions")

    @property
    def get_choices(self):
        return self.choices.split(',') if self.choices else []
    
    def __str__(self):
        return self.text

class Submission(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE, related_name='submissions')
    submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

class Answer(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()

    def __str__(self):
        return f"{self.question.text}: {self.answer_text}"

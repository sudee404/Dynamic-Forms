# forms.py
from django import forms
from .models import Form, Question

class FormCreationForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class QuestionCreationForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'question_type', 'choices']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'question_type': forms.Select(attrs={'class': 'form-control'}),
            'choices': forms.Textarea(attrs={'class': 'form-control'}),
        }

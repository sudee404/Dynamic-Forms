from django.shortcuts import render, redirect
from .models import Form, Submission, Answer
from .forms import FormCreationForm, QuestionCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')


def create_form(request):
    if request.method == 'POST':
        form = FormCreationForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.owner = request.user
            form_instance.save()
            return redirect('form_detail', form_id=form_instance.id)
    else:
        form = FormCreationForm()
    return render(request, 'forms/form_create.html', {'form': form})

def add_question(request, form_id):
    form_instance = Form.objects.get(id=form_id)
    if request.method == 'POST':
        question_form = QuestionCreationForm(request.POST)
        if question_form.is_valid():
            question = question_form.save(commit=False)
            question.form = form_instance
            question.save()
    else:
        question_form = QuestionCreationForm()
    return render(request, 'forms/form_detail.html', {'form': form_instance, 'question_form': question_form})

def submit_form(request, form_id):
    form_instance = Form.objects.get(id=form_id)
    if request.method == 'POST':
        submission = Submission.objects.create(form=form_instance, submitted_by=request.user if request.user.is_authenticated else None)
        for question in form_instance.questions.all():
            print(question,f'answers_{question.id}',request.POST.get(f'answers_{question.id}'))
            answer_text = request.POST.get(f'answers_{question.id}')
            Answer.objects.create(submission=submission, question=question, answer_text=answer_text)
        return redirect('submission_detail', submission_id=submission.id)
    return render(request, 'submit_form.html', {'form': form_instance})
    
# views.py
def my_submissions(request):
    submissions = Submission.objects.filter(submitted_by=request.user)
    return render(request, 'submissions/my_submissions.html', {'submissions': submissions})

def form_submissions(request, form_id):
    form_instance = Form.objects.get(id=form_id)
    if request.user != form_instance.owner:
        return redirect('home')
    submissions = form_instance.submissions.all()
    return render(request, 'submissions/submissions.html', {'form': form_instance, 'submissions': submissions})

def submission_detail(request, submission_id):
    submission = Submission.objects.get(id=submission_id)
    return render(request, 'submissions/submission_detail.html', {'submission': submission})

@login_required
def list_forms(request):
    forms = Form.objects.filter(owner=request.user)
    return render(request, 'forms/form_list.html', {'forms': forms})

def form_detail(request, form_id):
    form_instance = Form.objects.get(id=form_id)
    question_form = QuestionCreationForm()
    return render(request, 'forms/form_detail.html', {'form': form_instance, 'question_form': question_form})


def form_view(request, form_id):
    form_instance = Form.objects.get(slug=form_id)
    return render(request, 'forms/form_view.html', {'form': form_instance})


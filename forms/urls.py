from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('forms/', views.list_forms, name='forms'),
    path('forms/new/', views.create_form, name='create_form'),
    path('forms/<int:form_id>/', views.form_detail, name='form_detail'),
    path('forms/<int:form_id>/add-question/', views.add_question, name='add_question'),
    path('forms/<int:form_id>/submit/', views.submit_form, name='submit_form'),
    path('forms/<int:form_id>/submissions/', views.view_submissions, name='view_submissions'),
    path('submissions/', views.view_submissions, name='submissions'),
]
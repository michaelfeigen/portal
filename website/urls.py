"""
This module contains all the paths for the website app.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='wiredrive'), 
    path('form/', views.getForm, name='form'),
    path('info/', views.getInfo, name='info'),
    path('casestudy/', views.CaseStudyView.as_view(), name='case study'),
    path('casestudy/questions', views.getQuestions, name='questions'),
    ]
"""
This module contains all the paths for the social app.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='social'),
    path('form/', views.getForm, name='form'),
    ]
"""
This module contains all the paths for the form app.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.getName, name='getName'),
    path('masters/', views.CheckView.as_view(), name = 'master')
]
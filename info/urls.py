"""
This module contains all the paths for the info app.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getName, name='info'), 
    ]
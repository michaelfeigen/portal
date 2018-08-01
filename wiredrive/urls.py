"""
This module contains all the paths for the wiredrive app.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='wiredrive'),
    path('form/', views.getName, name='get_name'),
    path('list/', views.getCheck, name = 'checklist'),
    path('credits/', views.getCredit, name = 'credits'),
    path('path/', views.getPath, name = 'path')
]
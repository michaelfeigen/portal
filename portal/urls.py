"""
This module contains all the paths for the project.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
	path('form/', include('form.urls')),
	path('wiredrive/', include('wiredrive.urls')),
	path('website/', include('website.urls')),
	path('social/', include('social.urls')),
	path('exit/', include('exit.urls')),
	path('info/', include('info.urls')),
    path('admin/', admin.site.urls),
]

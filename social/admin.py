"""
This module registers the models with the admin site 
so that you can view and edit the content of your Models 
on the admin site.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.contrib import admin

from .models import social

admin.site.register(social)

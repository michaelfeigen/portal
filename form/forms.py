"""
This module contains classes that describe a form and determines how it works.
Each class contains fields that map to HTML form <input> elements. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.forms import ModelForm, widgets
from .models import job


class UserForm(ModelForm):

	class Meta:
		#the model to use
		model = job
		#the fields in the model that you want your HTML form to have access to
		fields = ['jobName', 'jobId']


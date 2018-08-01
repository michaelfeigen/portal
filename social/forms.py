"""
This module contains classes that describe a form and determines how it works.
Each class contains fields that map to HTML form <input> elements. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.forms import ModelForm
from .models import social


class socialForm(ModelForm):
	
	class Meta:
		#the model to use
		model = social
		#the field in the model you don't want your HTML form to have access to
		exclude = ['jobId']



"""
This module contains classes that describe a form and determines how it works.
Each class contains fields that map to HTML form <input> elements. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.forms import ModelForm
from django import forms 


class infoForm(forms.Form):
	#the field that you want your HTML form to have access to
	jobId = forms.IntegerField()


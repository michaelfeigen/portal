"""
This module contains classes that describe a form and determines how it works.
Each class contains fields that map to HTML form <input> elements. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.forms import ModelForm
from .models import wiredrive, checklist, credit, filePath


class wiredriveForm(ModelForm):
	
	class Meta:
		#the model to use
		model = wiredrive
		#the fields in the model that you want your HTML form to have access to
		fields = ['title', 'isciId', 'jobId']


class CheckForm(ModelForm):

	class Meta:
		#the model to use
		model = checklist
		#the field in the model you don't want your HTML form to have access to
		exclude = ['wiredriveId']


class CreditForm(ModelForm):

	class Meta:
		#the model to use
		model = credit
		#the field in the model you don't want your HTML form to have access to
		exclude = ['wiredriveId']


class PathForm(ModelForm):

	class Meta: 
		#the model to use
		model = filePath
		#the fields in the model that you want your HTML form to have access to
		fields = ['thumbnailPath', 'specPath']

	
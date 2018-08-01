"""
This module contains classes that describe a form and determines how it works.
Each class contains fields that map to HTML form <input> elements. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.forms import ModelForm
from .models import website, caseStudy   


class websiteForm(ModelForm):
	
	class Meta:
		#the model to use
		model = website 
		#the fields in the model that you want your HTML form to have access to
		fields = ['vimeoPath', 'labPage', 'vfxPage', 'colorPage', 
				  'thumbnailImagePath', 'rolloverGifPath']


class caseStudyForm(ModelForm):
	
	class Meta:
		#the model to use
		model = caseStudy
		#the fields in the model that you want your HTML form to have access to
		fields = ['first', 'second', 'third', 'question2', 
				  'question3', 'artistQuote', 'directorQuote']

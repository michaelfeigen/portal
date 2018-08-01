"""
This module controls what appears on screen and allows you to record data the user
enters on the web page. A view is simply a function or class that takes a Web request 
and returns a Web response.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.views import generic, View
from .forms import websiteForm, caseStudyForm
from .models import website, caseStudy
from form.models import job


class IndexView(View):

	def get(self, request):
		"""
		Parameter request: a web request
		Returns: a Web response 
		"""
		return render_to_response('website/index.html')


class CaseStudyView(View):

	def get(self, request):
		"""
		Parameter request: a web request
		Returns: a Web response 
		"""
		return render_to_response('website/caseStudy.html')


def getQuestions(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""

	#check if a form entry already exists for the current website ID and if so delete it
	try:
		key = caseStudy.objects.get(websiteId = website.objects.latest('id'))
		key.delete()
	except:
		pass

	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = caseStudyForm(request.POST)
		
		if form.is_valid():
			#save the information to the database
			formItem = form.save(commit=False)
			formItem.websiteId = website.objects.latest('id')
			formItem.save()
			return redirect('/social')
	
	# if a GET (or any other method) we'll create a blank form
	else:
		form = caseStudyForm()

	return render(request, 'website/questions.html', {'form': form} )


def getForm(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""

	#check if a form entry already exists for the current job ID and if so delete it
	try:
		key = website.objects.get(jobId = job.objects.latest('id'))
		key.delete()
	except:
		pass

	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = websiteForm(request.POST)

		if form.is_valid():
			#save the information to the database
			formItem = form.save(commit=False)
			formItem.jobId = job.objects.latest('id')
			formItem.save()
			return redirect('/website/info')
	
	# if a GET (or any other method) we'll create a blank form
	else:
		form = websiteForm()

	return render(request, 'website/info.html', {'form': form} )


def getInfo(request):
	"""
	Parameter request: a web request
	Returns: a Web response 
	"""
	return redirect('/website/casestudy')

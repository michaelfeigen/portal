"""
This module controls what appears on screen and allows you to record data the user
enters on the web page. A view is simply a function or class that takes a Web request 
and returns a Web response.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views import generic, View
from .forms import UserForm
from .models import job


class CheckView(View):

	def get(self, request):
		"""
		Parameter request: a web request
		Returns: a Web response 
		"""
		return render_to_response('form/check.html')


def getName(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""

	#check if the Job ID entered already exists and if so delete the existing job 
	try:
		formId = request.POST.get('jobId')
		key = job.objects.get(jobId = formId)
		key.delete()
	except:
		pass

	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = UserForm(request.POST)

		if form.is_valid():
			#save the information to the database
			formItem = form.save(commit=False)
			formItem.save()
			return render_to_response('form/master.html')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = UserForm()

	return render(request, 'form/index.html', {'form': form} )
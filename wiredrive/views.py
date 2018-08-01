"""
This module controls what appears on screen and allows you to record data the user
enters on the web page. A view is simply a function or class that takes a Web request 
and returns a Web response.

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.conf import settings 
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, redirect
from django.views import generic, View
from .forms import wiredriveForm, CheckForm, CreditForm, PathForm
from .models import wiredrive, checklist, credit, filePath


class IndexView(View):

	def get(self, request):
		"""
		Parameter request: a web request
		Returns: a Web response 
		"""
		return render_to_response('wiredrive/index.html')


def getCheck(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""

	#check if a form entry already exists for the current wiredrive ID and if so delete it
	try:
		key = checklist.objects.get(wiredriveId = wiredrive.objects.latest('id'))
		key.delete()
	except:
		pass

	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = CheckForm(request.POST)

		if form.is_valid():
			#save the information to the database
			formItem = form.save(commit=False)
			formItem.wiredriveId = wiredrive.objects.latest('id')
			formItem.save()
			return redirect('/wiredrive/credits')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = CheckForm()

	return render(request, 'wiredrive/checklist.html', {'form': form} )


def getPath(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""

	#check if a form entry already exists for the current wiredrive ID and if so delete it
	try:
		key = filePath.objects.get(wiredriveId = wiredrive.objects.latest('id'))
		key.delete()
	except:
		pass

	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = PathForm(request.POST)

		if form.is_valid():
			#save the information to the database
			formItem = form.save(commit=False)
			formItem.wiredriveId = wiredrive.objects.latest('id')
			formItem.save()
			return redirect('/website')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = PathForm()

	return render(request, 'wiredrive/path.html', {'form': form})


def getCredit(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""

	#check if a form entry already exists for the current wiredrive ID and if so delete it
	try:
		key = credit.objects.get(wiredriveId = wiredrive.objects.latest('id'))
		key.delete()
	except:
		pass

	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = CreditForm(request.POST)

		if form.is_valid():
			#save the information to the database
			formItem = form.save(commit=False)
			formItem.wiredriveId = wiredrive.objects.latest('id')
			formItem.save()
			return redirect('/wiredrive/path')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = CreditForm()

	return render(request, 'wiredrive/credits.html', {'form': form})


def getName(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""

	#check if a form entry already exists for the current job ID and if so delete it
	try:
		formId = request.POST.get('jobId')
		key = wiredrive.objects.get(jobId = formId)
		key.delete()

	except:
		pass

	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = wiredriveForm(request.POST)

		if form.is_valid():
			#save the information to the database
			formItem = form.save(commit=False)
			formItem.save()

			#set the arguments to pass into send_mail
			subject = 'Carbon Portal'
			message = 'Title: ' + str(formItem.title) +  '\nJob ID: ' + str(formItem.jobId_id) + '\nISCI ID: ' + str(formItem.isciId)
			fromEmail = settings.EMAIL_HOST_USER
			toList = ['mfeigen@carbonvfx.com'] 

			#send an email to toList
			send_mail(subject, message, fromEmail, toList, fail_silently = True)

			return redirect('/wiredrive/list')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = wiredriveForm()

	return render(request, 'wiredrive/email.html', {'form': form})
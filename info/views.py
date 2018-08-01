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
from .forms import infoForm
from form.models import job
from wiredrive.models import wiredrive, checklist, credit, filePath
from website.models import website, caseStudy
from social.models import social


class IndexView(View):

	def get(self, request):
		"""
		Parameter request: a web request
		Returns: a Web response 
		"""
		return render_to_response('info/index.html')


def getName(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""
	dataDict = {}
	validID = False

	#check if the job ID entered is valid 
	try:
		formId = request.POST.get('jobId')
		key = job.objects.get(jobId= formId)
		validID = True
	except:
		pass

	if request.method == 'POST' and validID:
		# create a form instance and populate it with data from the request
		form = infoForm(request.POST)

		if form.is_valid():

			#add models that exist and are associated with the valid Job ID entered
			try:
				dataDict['data'] = job.objects.get(jobId=formId)
				dataDict['wiredriveData'] = wiredrive.objects.get(jobId = formId)
				dataDict['checklistData'] = checklist.objects.get(wiredriveId = dataDict['wiredriveData'].id)
				dataDict['creditData'] = credit.objects.get(wiredriveId =  dataDict['wiredriveData'].id)
				dataDict['filePathData'] = filePath.objects.get(wiredriveId = dataDict['wiredriveData'].id)
				dataDict['websiteData'] = website.objects.get(jobId = formId)
				dataDict['caseStudyData'] = caseStudy.objects.get(websiteId = dataDict['websiteData'].id)
			except:
				pass
			
			try: 
				dataDict['socialData'] = social.objects.get(jobId = formId)
			except:
				pass
	
			return render(request, 'info/data.html', dataDict )
	
	# if a GET (or any other method) or the ID is not valid we'll create a blank form
	else:
		form = infoForm()

	return render(request, 'info/index.html', {'form': form} )



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
from .forms import socialForm
from .models import social
from form.models import job


class IndexView(View):

	def get(self, request):
		"""
		Parameter request: a web request
		Returns: a Web response 
		"""
		return render_to_response('social/index.html')


def getForm(request):
	"""
	Takes information entered in the form and if it is valid adds it to the database.

	Parameter request: a web request
	Returns: a Web response 
	"""

	#check if a form entry already exists for the current job ID and if so delete it
	try:
		key = social.objects.get(jobId = job.objects.latest('id'))
		key.delete()
	except:
		pass

	if request.method == 'POST':
		# create a form instance and populate it with data from the request
		form = socialForm(request.POST)

		if form.is_valid():
			#save the information to the database
			formItem = form.save(commit=False)
			formItem.jobId = job.objects.latest('id')
			formItem.save()

			#set the arguments to pass into send_mail
			subject = 'Carbon Portal'
			message = ('Platform: ' + str(formItem.platform)
				       + '\nQuote from agency CD/Director/Client: ' + str(formItem.quote)
				       + '\n\nGeneral ' + '\nOffice: ' + str(formItem.office) + '\nContact:' + str(formItem.contact)
				       + '\nProject Name: ' + str(formItem.projectName) + '\nFilters: (Featured/VFX/Color)' + str(formItem.filters)
				       + '\n\nCredits' + '\nProduction Company: ' + str(formItem.productionCompanyName) + '\nDirector: '
				       + str(formItem.directorName) + '\nAgency: ' + str(formItem.agencyName) + '\nClient: ' 
				       + str(formItem.clientName) + '\nProduct: ' + str(formItem.productName) 
				       + '\n\nWhat is this project about? What was the creative brief like?\n\n' + str(formItem.question1)  + '\n\nWhat was Carbon’s speciic role in this project?\n\n' 
				       + str(formItem.question2)  + '\n\nWho are the key agency/creatives we should mention?\n\n' + str(formItem.question3)
			           + '\n\nWhat aspects of the project should we focus on?\n\n' + str(formItem.question4)  + '\n\nIs there anything technically interesting worth noting?\n\n' 
			           + str(formItem.question5)  + '\n\nWhat are some highlights from the production?\n\n' + str(formItem.question6) + '\n\nWhat was the collaborative process like?\n\n' 
			           + str(formItem.question7)  + '\n\nWere there any technical challenges?\n\n' + str(formItem.question8)  
			           + '\n\nIs there anything else you feel is important to mention?\n\n' + str(formItem.question9))
			fromEmail = settings.EMAIL_HOST_USER
			toList = ['mfeigen@carbonvfx.com'] 

			#send an email to toList
			send_mail(subject, message, fromEmail, toList, fail_silently = True)

			return redirect('/exit')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = socialForm()

	return render(request, 'social/questions.html', {'form': form} )
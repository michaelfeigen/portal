"""
This module contains the essential fields and behaviors of the PR & Social data
you are storing in your database. Each model is represented by a class that
subclasses django.db.models.Model and is a seperate table in your database.
Each model has a number of class variables, each of which represents a field 
in that table. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.db import models


class social(models.Model):
	"""
	This class represents a table in your database. An instance of this class
	represents a row in that table.

	This class extends models.Model.
	"""

	#set table fields
	platform = models.CharField(max_length = 100, null = True, blank = True)
	quote = models.CharField(max_length = 500, null = True, blank = True)
	office = models.CharField(max_length = 100, null = True, blank = True)
	contact = models.CharField(max_length = 100, null = True, blank = True)
	projectName = models.CharField(max_length = 100, null = True, blank = True)
	filters = models.CharField(max_length = 100, null = True, blank = True)
	productionCompanyName = models.CharField(max_length = 100, null = True, blank = True)
	directorName = models.CharField(max_length = 100, null = True, blank = True)
	agencyName = models.CharField(max_length = 100, null = True, blank = True)
	clientName = models.CharField(max_length = 100, null = True, blank = True)
	productName = models.CharField(max_length = 100, null = True, blank = True)
	question1 = models.CharField(max_length = 2000, null = True, blank = True)
	question2 = models.CharField(max_length = 2000, null = True, blank = True)
	question3 = models.CharField(max_length = 2000, null = True, blank = True)
	question4 = models.CharField(max_length = 2000, null = True, blank = True)
	question5 = models.CharField(max_length = 2000, null = True, blank = True)
	question6 = models.CharField(max_length = 2000, null = True, blank = True)
	question7 = models.CharField(max_length = 2000, null = True, blank = True)
	question8 = models.CharField(max_length = 2000, null = True, blank = True)
	question9 = models.CharField(max_length = 2000, null = True, blank = True)
	jobId = models.ForeignKey('form.job',  to_field="jobId", on_delete = models.CASCADE)

	#set the name of the table
	class Meta:
		db_table = 'social'


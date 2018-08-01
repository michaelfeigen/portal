"""
This module contains the essential fields and behaviors of the form data
you are storing in your database. Each model is represented by a class that
subclasses django.db.models.Model and is a seperate table in your database.
Each model has a number of class variables, each of which represents a field 
in that table. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.db import models


class job(models.Model):
	"""
	This class represents a table in your database. An instance of this class
	represents a row in that table.

	This class extends models.Model.
	"""

	#set table fields
	jobName = models.CharField(max_length = 100)
	jobId = models.PositiveIntegerField(unique = True)

	#override the string method
	def __str__(self):
		return self.jobName

	#set the name of the table
	class Meta:
		db_table = 'job'


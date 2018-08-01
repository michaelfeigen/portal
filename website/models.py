"""
This module contains the essential fields and behaviors of the website data
you are storing in your database. Each model is represented by a class that
subclasses django.db.models.Model and is a seperate table in your database.
Each model has a number of class variables, each of which represents a field 
in that table. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.db import models


class website(models.Model):
	"""
	This class represents a table in your database. An instance of this class
	represents a row in that table.

	This class extends models.Model.
	"""

	#set table fields
	vimeoPath = models.CharField(max_length = 300, null = True, blank = True)
	labPage = models.BooleanField()
	vfxPage = models.BooleanField()
	colorPage = models.BooleanField()
	thumbnailImagePath = models.CharField(max_length = 300, null = True, blank = True)
	rolloverGifPath = models.CharField(max_length = 300, null = True, blank = True)
	jobId = models.ForeignKey('form.job', to_field="jobId", on_delete = models.CASCADE)

	#set the name of the table
	class Meta:
		db_table = 'website'


class caseStudy(models.Model):
	"""
	This class represents a table in your database. An instance of this class
	represents a row in that table.

	This class extends models.Model.
	"""

	#set table fields
	websiteId = models.ForeignKey('website', on_delete = models.CASCADE)
	first = models.CharField(max_length = 2000, null = True, blank = True)
	second = models.CharField(max_length = 2000, null = True, blank = True)
	third = models.CharField(max_length = 2000, null = True, blank = True)
	question2 = models.CharField(max_length = 2000, null = True, blank = True)
	question3 = models.CharField(max_length = 2000, null = True, blank = True)
	artistQuote = models.CharField(max_length = 2000, null = True, blank = True)
	directorQuote = models.CharField(max_length = 2000, null = True, blank = True)

	#set the name of the table
	class Meta:
		db_table = 'caseStudy'



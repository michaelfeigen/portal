"""
This module contains the essential fields and behaviors of the wiredrive data
you are storing in your database. Each model is represented by a class that
subclasses django.db.models.Model and is a seperate table in your database.
Each model has a number of class variables, each of which represents a field 
in that table. 

Name: Michael Feigen
Date Completed: 7/31/2018
"""
from django.db import models


class wiredrive(models.Model):
	"""
	This class represents a table in your database. An instance of this class
	represents a row in that table.

	This class extends models.Model.
	"""

	#set table fields
	isciId = models.CharField(max_length = 100, null = True, blank = True)
	title = models.CharField(max_length = 100)
	jobId = models.ForeignKey('form.job',  to_field="jobId", on_delete = models.CASCADE)

	#override the string method
	def __str__(self):
		return self.title

	#set the name of the table
	class Meta:
		db_table = 'wiredrive'


class checklist(models.Model):
	"""
	This class represents a table in your database. An instance of this class
	represents a row in that table.

	This class extends models.Model.
	"""

	#set table fields
	wiredriveId = models.ForeignKey('wiredrive', on_delete = models.CASCADE) 
	
	#Headline Search terms for content
	keyVisualContent = models.CharField(max_length = 200, null = True, blank = True)
	famousTalent = models.CharField(max_length = 200, null = True, blank = True)

	#Format
	film = models.BooleanField()
	TV = models.BooleanField()
	web = models.BooleanField()
	social = models.BooleanField()
	musicVideo = models.BooleanField()
	shortFilm = models.BooleanField()
	feature = models.BooleanField()
	computerGame = models.BooleanField()
	VR = models.BooleanField()
	PSA = models.BooleanField()
	comedy = models.BooleanField()
	celebrity = models.BooleanField()

	#Categories broken down by creative content
	design = models.BooleanField()
	animation = models.BooleanField()
	character = models.BooleanField()
	handDrawn = models.BooleanField()
	collage = models.BooleanField()
	illustration = models.BooleanField()
	mixedMedia = models.BooleanField()
	stylized = models.BooleanField()
	graphic = models.BooleanField()
	logo = models.BooleanField()
	craft = models.BooleanField()	
	handMade = models.BooleanField()
	practical = models.BooleanField()
	paper = models.BooleanField()
	text = models.BooleanField()
	motionGraphics = models.BooleanField()

	#Direction
	supervision = models.BooleanField()
	shoot = models.BooleanField()
	tableTop = models.BooleanField()
	model = models.BooleanField()
	stopFrame = models.BooleanField()
	product = models.BooleanField()
	packShot = models.BooleanField()

	#2D
	VFX = models.BooleanField()
	visualEffects = models.BooleanField()
	compositing = models.BooleanField()
	photoReal = models.BooleanField()
	cleanUp = models.BooleanField()
	screenReplace = models.BooleanField()
	integration = models.BooleanField()
	timelapse = models.BooleanField()
	projection = models.BooleanField()
	retouch = models.BooleanField()
	beautyRetouching = models.BooleanField()
	endTag2D = models.BooleanField()

	#3D
	CGI = models.BooleanField()
	mattePainting = models.BooleanField()
	simulation = models.BooleanField()
	water = models.BooleanField()
	liquids = models.BooleanField()
	particles = models.BooleanField()
	smoke = models.BooleanField()
	cloth = models.BooleanField()
	shatter = models.BooleanField()
	fire = models.BooleanField()
	photoscan = models.BooleanField()
	crowd = models.BooleanField()
	stadium = models.BooleanField()
	environment = models.BooleanField()
	fur = models.BooleanField()
	hair = models.BooleanField()
	creature = models.BooleanField()
	setExtension = models.BooleanField()
	endTag3D = models.BooleanField()

	#Color
	grade = models.BooleanField()
	grading = models.BooleanField()
	colorist = models.BooleanField()
	beauty = models.BooleanField()

	#Common recurring genres
	automotive = models.BooleanField()
	fashion = models.BooleanField()
	sport = models.BooleanField()
	blank = models.BooleanField()
	pharma = models.BooleanField()
	food = models.BooleanField()
	technology = models.BooleanField()

	#set the name of the table
	class Meta:
		db_table = 'checklist'


class credit(models.Model):
	"""
	This class represents a table in your database. An instance of this class
	represents a row in that table.

	This class extends models.Model.
	"""

	#set table fields
	wiredriveId = models.ForeignKey('wiredrive', on_delete = models.CASCADE)
	carbonCdName = models.CharField(max_length = 100, null = True, blank = True)
	clientName = models.CharField(max_length = 100, null = True, blank = True)
	directorName = models.CharField(max_length = 100, null = True, blank = True)
	productionCompanyName = models.CharField(max_length = 100, null = True, blank = True)
	coloristName = models.CharField(max_length = 100, null = True, blank = True)
	productName = models.CharField(max_length = 100, null = True, blank = True)
	filmTitle = models.CharField(max_length = 100, null = True, blank = True)

	#set the name of the table
	class Meta:
		db_table = 'credits'


class filePath(models.Model):
	"""
	This class represents a table in your database. An instance of this class
	represents a row in that table.

	This class extends models.Model.
	"""

	#set table fields
	wiredriveId = models.ForeignKey('wiredrive', on_delete = models.CASCADE)
	thumbnailPath = models.CharField(max_length = 200, null = True, blank = True)
	specPath = models.CharField(max_length = 200, null = True, blank = True)

	#set the name of the table
	class Meta:
		db_table = 'filePath'


# Carbon VFX Portal 

Web application built with [Python 3.7](https://www.python.org/downloads/release/python-370/) and the [Django 2.0.7](https://www.djangoproject.com/download/) web framework. It includes background video, auto generated emails, SQLite database and a web page for viewing database content. 

<img src="/form/static/form/img/loop.gif">

## Motivation
Portal is a web application that's designed to streamline the job completion process at Carbon VFX, a visual effects and motion graphics company. Essentially, when a project is finished, producers go on the web app and fill out the required information forms. The web app automatically generates emails and sends the relevant information to the right people. Later, when producers want to see information about a particular job, they can come back to the web app and view their colleagues' answers. 


## Demo

### Portal Form

click [here](https://www.youtube.com/watch?v=SbSJWxvMICU&feature=youtu.be) to watch the full demo. 

<img src="/form/static/form/img/form.gif">

### Portal Database Viewer

click [here](https://www.youtube.com/watch?v=ukomRNCrmWA&feature=youtu.be) to watch the full demo. 

<img src="/form/static/form/img/DbView.gif">


## Getting Started

These instructions will get a copy of the project up and running on your local machine.


### Installation

After installing Python, go to the directory in which you downloaded the project. For example, if your directory is called portal:
```
cd portal
```
Run the following command to install Django:
```
pip install django
```

Some of these applications use at least one database table, so we need to create the tables in the databse before we can use them. To do that run the following command:
```
python manage.py makemigrations
python manage.py migrate
```
Also note that anytime you change something in models.py you must run these same commands.

Then run the following command and make sure you go to **/form**:
```
python manage.py runserver
```
Once the website is running, you can interact with it and fill out the form(s).

To see the data you entered, go to /info.

## How to use 

If you are new to Django, a great tutorial that will familiarize you with how things work, can be found [here](https://docs.djangoproject.com/en/2.0/intro/tutorial01/). Once you understand the basics, it shouldn't be too difficult to navigate through the project. Django organizes things through apps. To create a new app, simply write:

```
python manage.py startapp appname
```
There are several things you must do when creating new apps and a full tutorial can be found [here](https://docs.djangoproject.com/en/2.0/intro/tutorial01/). In this project, the different apps are form, info, website, wiredrive and social. Inside each app, there is a folder called templates. All HTML files are always stored inside the templates folder. Additionally, each app contains a module called views.py. This module controls what HTML templates get loaded onto the screen and how you interact with the web application. Furthermore, each app contains a module called models.py where you can organize how you want your database to look and how you want to store each app's data. 

If you are interested in style, everything that has to do with how the page looks can be found in forms/static. 

### Auto generated email configuration 
To create auto-generated emails, open settings.py inside the portal folder. In this module, you will find the following at the bottom:
```
EMAIL_USE_TLS = True 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yourgmail@gmail.com'
EMAIL_HOST_PASSWORD = 'YourPassword'
EMAIL_PORT = 587
```
Simply fill in the information of the gmail account you want the emails to be sent from. Next, in order to send the emails, you must go into your views.py and make sure you have the following imported:
```
from django.core.mail import send_mail
```
Once you have this imported, you can then fill out the email's subject, message, sender and reciver as follows:
```
send_mail(subject, message, fromEmail, toList, fail_silently = True)
```
A good exapmle of this can be found in the wiredrive/views.py.

## Authors

* **Michael Feigen** 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

<img src="/form/static/form/img/thanks.gif">


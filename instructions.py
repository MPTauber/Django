############ SET-UP
## py -3 -m venv django_venv
## django_venv/scripts/activate
## pip install django

############ CREATE THE DJANGO PROJECT
# Create a new project called learning_log
### django-admin startproject learning_log .
# Dot is important!! Creates it with a directory structure.

############ CREATE THE DATABASE
# Django stores most of the information for 
# a project in a database:
### py manage.py migrate
# Typically the migrate command is used to modify a database.
# This creates a new SQLite database because it is used for the first time (db.sqlite3)
# Ideal for simple apps

############ VIEW THE PROJECT
# Verify that everything is set up correctly:
### py manage.py runserver
# Click http://127.0.0.1:8000/ to check
# Press CTRL+C in terminal window to quit

############ CREATE A DEBUGGER LAUNCH PROFILE
## Switch to Run view to create launch.json (instuctions in ppt Django I)

############ STARTING AN APP
# A Django project is organized as a group of individual apps that work
# together to make the project work as a whole.

# Create a structure for the app
### py manage.py startapp learning_logs
# Creates a directory called learning_logs which has several files in it

############ DEFINING THE MODEL
# Now, use models.py in learning_logs to define the data we want to manage in our app.
# A model tells Django how to work with the data that will be stored in the app
# For our project we want the user to be able to create a number of topics for their journal (learning_log). 
# So each entry will have a topic, text and timestamp
# Code-wise, a model is just a class; it has attributes and methods

# For the entire list of fields for models:
# https://docs.djangoproject.com/en/2.2/ref/models/fields/

############ ACTIVATING THE MODEL
# Open settings.py in learning_log to add the app we created:
''' 
INSTALLED_APPS = [
    #my_apps
    'learning_logs',
    etc. 
'''

############ STORING THE INFORMATION
# Modify the database to store information related to the model - Topic
### py manage.py makemigrations learning_logs
# This command creates a migration file that instructs the database to store any
# data associated with any new models.
### py manage.py migrate
# This command applies the changes in the migration file previously created.

############ THE DJANGO ADMIN SITE
# Easily work with models in the admin site.
# Only an administrator should use this, not the public.
# Create a super user that has access to all the infromation stored on the site.
### py manage.py createsuperuser
# password: mypassword1234

############  REGISTERING A MODEL WITH THE ADMIN SITE
# Django comes pre-built with the user and group models
# To use the Topic model, we have to register it with the admin site.
# The dot in front of models tells Django to look for models.py in the
# same directory as admin.py
# The code admin.site.register() tells Django to manage our model through the admin site.
### Go to admin.py in learning_logs and type code.
'''
from .models import Topic

admin.site.register(Topic)
'''
# To check if it worked run serverr agian and click link:
### py manage.py runserver
# Add /admin behind link in browser address
# http://127.0.0.1:8000/admin
# username: madeleine
# password: mypassword1234

############ ADDING TOPICS
# Click Topics
# "Add Topic +" pill
# Added topics "Chess" and "Rock Climbing"

############ DEFINING THE ENTRY MODEL
# We need to define a model for the kinds of entries 
# users can make in their learning logs.
# Each entry needs to be associated with a particular topic
# This relationship is called a many-to-one relationship, meaning many entries can be associated with one topic.

# Use models.py.
''' 
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeFIeld(auto_now_add=True)

    class Meta:
        # it allows us to set a special attribute telling Django to use "Entries"
        # when it needs to refer to more than one entry. Without this, Django
        # would refer to multiple entries as "Entrys".
        verbose_name_plural = "entries"

    def __str__(self):
        return f"{self.text[:50]}..."
'''
# "topic" is a foreign key. We cascade when deleting, so both get deleted.

############ MIGRATE AND REGISTER THE ENTRY MODEL
# In terminal: 
###py manage.py makemigrations learning_logs
### py manage.py migrate
# In admin.py
'''
from .models import Entry

admin.site.register(Entry)
'''
# Or add Entry after Topic: 
# from .models import Topic, Entry

############ THE DJANGO SHELL
# To examine data programmatically (manually not with server) through an interactive terminal session:
# Create the Django Shell --> MyShell.py
# Add code and run. 
# Can be found in MyShell.py

############ MAKING PAGES
# Consists out of three stages in Django:
# 1. Defining URLs
# 2. Writing views
# 3. Writing tmplates

# Each URL maps to a view
# The view function retrieves and processes the data needed for that page.
# The view function often renders the page using a template, which contains
# the overall structure of the page.

############ MAPPING THE URL
# Map the home page URL to something other than the default Django site (With the rocket)
# Edit the default urls.py file in the learning_log folder to look like this:
'''
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("learning_logs.urls")),
]
'''
# This says that we create another pathway in our app (learning_logs - not in our project learning_log)
# That command makes it know where to go

# Make a new file, urls.py, in the learning-logs folder (the app)
#### Go into urls.py (in learning_logs) to find instructions there.

############ WRITING A VIEW
# A view function takes in information from a request, prepares the data needed to
# generate a page, and then sends the data abck to the browser,
# often by using a template that defined what the page will look like.

# When a URL request matches the pattern we just defined in urlss.py (learning_logs),
# Django looks for a function called index() in the views.py file.
# Check "def index(request):" line at views.py

############ WRITING A TEMPLATE
# Defines what the page should look like, and Django fills in 
# the relevant data each time the page is requested.

# A template allows you to access any data provided by the view.

# Inside the learning_logs folder, make a new folder calles templates.
# Inside the templates folder, make another folder called learning_logs.
# Inside this inner learning_logs folder, make a new file called index.html.
# Then add html (find it in file)

############ TEMPLATE INHERITANCE
# Create a new template called base.html
# Change index.html to inherit from base.html (see file) --> it's now a child template
# base.py is the parent template.
# The add base.html to urls.py and views.py
# We also create a new child template called topics.html and add that stuff to views.py and urls.py too.
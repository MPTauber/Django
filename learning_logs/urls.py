# the path function, which is needed when mapping URLs ot views
from django.urls import path

# the dot tells Python to import the views.py module from
# the same directory as the current urls.py module.
from . import views

# The variable app_name helps Django distinguish this urls.py file from
# files of the same name in other apps within the project.
app_name = "learning_logs"

# The variable urlpatterns in this module is a list of individual pages
# that can be requested from the learning_logs app.
urlpatterns = [
    # the first argument is an empty string ("") which matches the
    # base URL - http://localhost:88000/. 
    # The second argument specifies the function name to call in views.py
    # The third argument provides the name " index" for this URL pattern to refer to it later
    path("", views.index, name="index"),
    path("topics", views.topics, name="topics"),
    path("topics/<int:topic_id>/", views.topic, name="topic"),
    path("new_topic/", views.new_topic, name="new_topic"),
    path("new_entry/<int:topic_id>/", views.new_entry, name="new_entry"),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name= 'edit_entry'),
]
# The next 4 lines are required word-for-word in the new Django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from learning_logs.models import Topic

topics = Topic.objects.all()

for topic in topics:
    print(topic.id, topic)

# If we know the ID of an object we can use the get() method to
# examine any attributes the object has.

t = Topic.objects.get(id=1) # Chess has ID of 1 (seen by executing the above for-loop)
print(t.text)
print(t.date_added)

# We can also look at the entries related to a certain topic.
# Since we defined topic as a foreignkey attribute in the Entry model,
# Django can use this relationship to access the entries for any topic.
# To get data through a foreign key relationship, you use the lowercase name
# of the related model followed by an underscore and the word set.

entries = t.entry_set.all() # t represents Chess cause we set it as id 1

for entry in entries:
    print(entry)
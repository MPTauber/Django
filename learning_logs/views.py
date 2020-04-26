from django.shortcuts import render

# Create your views here.

# When a URL request matches the pattern we just defined in urls.py (learning_logs),
# Django looks for a function called index() in the views.py file.

def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")

def base(request):
    """The base page for Learning Log."""
    return render(request, "learning_logs/base.html")

def topics(request):
    """The topics page for Learning Log"""
    return render(request, "learning_logs/topics.html")
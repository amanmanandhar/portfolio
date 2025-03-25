# portfolio/views.py
from django.shortcuts import render
from .models import Profile

def home(request):
    profile = Profile.objects.first()  # Get the first profile from the database
    return render(request, 'portfolio/home.html', {'profile': profile})

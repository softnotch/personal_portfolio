from django.shortcuts import render
from .models import Project
# from django.urls import path

# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})
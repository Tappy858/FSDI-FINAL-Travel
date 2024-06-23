from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    blog = Project.objects.all()
    return render(request, 'blog/home.html', {'blog': blog})

def about(request):
    return render(request, 'blog/about.html')

def projects_view(request):
    return render(request, 'blog/travel.html')
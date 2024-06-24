from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import *

# Create your views here.
def home(request):
    blog = Project.objects.all()
    return render(request, 'blog/home.html', {'blog': blog})

def about(request):
    return render(request, 'blog/about.html')

def projects_view(request):
    return render(request, 'blog/travel.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # You can customize the email content and settings as needed
        send_mail(
            f"Contact Form Submission from {name}",
            message,
            email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for your message. We will get back to you shortly.')
        return redirect('home')

    return render(request, 'blog/contact.html')
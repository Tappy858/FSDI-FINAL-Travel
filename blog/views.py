from django.shortcuts import render, redirect
from blog.forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from config import settings
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
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form_instance = form.save()

            # Retrieve cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email message
            email_subject = 'Contact Form Submission from {}'.format(name)
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            from_email = settings.EMAIL_HOST_USER
            to_email = 'test.mailtrap1234@gmail.com'  # Admin email

            # Send email
            email = EmailMessage(
                email_subject,
                email_message,
                from_email,
                [to_email],
                reply_to=[email]
            )
            email.send()

            # Display success message and redirect
            messages.success(request, 'Thank you for your message. We will get back to you shortly.')
            return redirect('home')
        else:
            messages.error(request, 'There was an error in your form. Please correct it and try again.')
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})
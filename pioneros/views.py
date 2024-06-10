from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def service(request):
    return render(request, "service.html")


def feature(request):
    return render(request, "feature.html")


def contact(request):
    if request.method == "POST":
        # Retrieve form data from POST request
        name = request.POST.get("nm")
        email = request.POST.get("em")
        subject = request.POST.get("sub")
        message = request.POST.get("mg")

        if name and email and service and message:

            Contact.objects.create(
                name=name, email=email, subject=subject, message=message
            )

            subject = "New Query Request Recieved"
            message_body = (
                f"Name: {name}\nEmail: {email}\nService: {service}\nMessage: {message}"
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['14ing.dev@gmail.com']

            send_mail(subject, message_body, from_email, recipient_list)
    return render(request, "contact.html")

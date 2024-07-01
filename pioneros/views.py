from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


# handel index page
def index(request):
    title = CustomizedERPTitle.objects.all()
    about = About.objects.all()
    about_content = About_Content.objects.all().order_by("-id")
    feature = Features.objects.all()
    service = Products.objects.all()
    carousel = Carousel.objects.all().order_by("-id")
    testimonial = Testimonial.objects.all().order_by("-id")
    erps = CustomizedERP.objects.all().order_by("-id")
    context = {
        "services": service,
        "carousels": carousel,
        "testimonials": testimonial,
        "erps": erps,
        "about": about,
        "abouts": about_content,
        "features": feature,
        "titles": title,
    }
    return render(request, "index.html", context)


# handel about page
def about(request):
    feature = Features.objects.all()
    about = About.objects.all().order_by("-id")
    about_content = About_Content.objects.all().order_by("-id")
    doctor = Doctor.objects.all().order_by("-id")
    context = {
        "doctors": doctor,
        "about": about,
        "abouts": about_content,
        "features": feature,
    }
    return render(request, "about.html", context)


# handel service page
def service(request):
    image = ServicesBackgroundImage.objects.first()
    hd = Header.objects.first()
    service = Services.objects.all()
    doctors = Doctor.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        "doctors": doctors,
        "services": service,
        "hds": hd,
        "testimonials": testimonial,
        "images": image,
    }  # Initialize context at the start

    if request.method == "POST":
        name = request.POST.get("nm")
        email = request.POST.get("em")
        phone = request.POST.get("ph")
        doctor_id = request.POST.get("doc")
        date1 = request.POST.get("date")
        date2 = request.POST.get("time")
        problem = request.POST.get("prob")

        if name and email and phone and doctor_id and date1 and date2 and problem:
            doctor = Doctor.objects.get(id=doctor_id)
            Appointment.objects.create(
                name=name,
                email=email,
                phone=phone,
                doctor=doctor,
                date=date1,
                time=date2,
                problems=problem,
            )

            subject = "New Appointment Received"
            message_body = f"Name: {name}\nEmail: {email}\nDoctor: {doctor.name}\nDate: {date1} {date2}\nProblem: {problem}"
            from_email = settings.EMAIL_HOST_USER
            recipient = ["14ing.dev@gmail.com"]
            send_mail(subject, message_body, from_email, recipient)

            messages.success(request, "Appointment booked successfully!")
            return redirect("service")  # Redirect back to the 'service' view
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, "service.html", context)


# handel product page
def product(request):
    image = ProductBackgroundImage.objects.first()
    hd = Header.objects.first()
    product = Products.objects.all()
    doctors = Doctor.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        "doctors": doctors,
        "products": product,
        "hds": hd,
        "testimonials": testimonial,
        "images": image,
    }  # Initialize context at the start

    if request.method == "POST":
        name = request.POST.get("nm")
        email = request.POST.get("em")
        phone = request.POST.get("ph")
        doctor_id = request.POST.get("doc")
        date1 = request.POST.get("date")
        date2 = request.POST.get("time")
        problem = request.POST.get("prob")

        if name and email and phone and doctor_id and date1 and date2 and problem:
            doctor = Doctor.objects.get(id=doctor_id)
            Appointment.objects.create(
                name=name,
                email=email,
                phone=phone,
                doctor=doctor,
                date=date1,
                time=date2,
                problems=problem,
            )

            subject = "New Appointment Received"
            message_body = f"Name: {name}\nEmail: {email}\nDoctor: {doctor.name}\nDate: {date1} {date2}\nProblem: {problem}"
            from_email = settings.EMAIL_HOST_USER
            recipient = ["14ing.dev@gmail.com"]
            send_mail(subject, message_body, from_email, recipient)

            messages.success(request, "Appointment booked successfully!")
            return redirect("product")  # Redirect back to the 'service' view
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, "product.html", context)


# handel feature page
def feature(request):
    # background_image = FeaturesBackgroundImage.objects.first()
    image = WarehouseAndLogistic.objects.all().order_by("-id")
    feature = Features.objects.all()
    features_content = Features_Content.objects.all().order_by("-id")
    context = {
        "features": feature,
        "features_contents": features_content,
        "warehouses": image,
    }
    return render(request, "feature.html", context)


# handel contact page
def contact(request):
    if request.method == "POST":
        # Retrieve form data from POST request
        name = request.POST.get("nm")
        email = request.POST.get("em")
        subjects = request.POST.get("sub")
        message = request.POST.get("mg")

        if name and email and subjects and message:

            Contact.objects.create(
                name=name, email=email, subject=subjects, message=message
            )
            subject = "New Query Request Recieved"
            message_body = (
                f"Name: {name}\nEmail: {email}\nSubject: {subjects}\nMessage: {message}"
            )
            from_email = settings.EMAIL_HOST_USER
            recipient = ["14ing.dev@gmail.com"]

            send_mail(subject, message_body, from_email, recipient)
            messages.success(request, "Your Query has been sent successfully!")
            return redirect("contact")  # Redirect back to the 'service' view
    return render(request, "contact.html", {"headers": Header.objects.all()})


@csrf_protect
def submit_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            # Save email to the database
            newsletter = Subscription(email=email)
            newsletter.save()
            return redirect("index")  # Redirect to a success page or the home page
    return HttpResponse("Invalid request", status=400)

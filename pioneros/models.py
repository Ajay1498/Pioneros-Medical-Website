from typing import Any
from django.db import models


# Create your models here.
class Header(models.Model):
    location = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    open = models.CharField(max_length=50)
    logo = models.ImageField(
        upload_to="images/headerlogo/", default=None, null=True, blank=True
    )
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    instagram_url = models.URLField(max_length=200, blank=True, null=True)
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)
    youtube_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.location


class Carousel(models.Model):
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to="images/carousels/")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Department(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(
        upload_to="images/doctors/", default=None, null=True, blank=True
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    facebook_url = models.URLField(max_length=200, blank=True, null=True)
    twitter_url = models.URLField(max_length=200, blank=True, null=True)
    instagram_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    
class CustomizedERPTitle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CustomizedERP(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.title
    

class ProductBackgroundImage(models.Model):
    image = models.ImageField(upload_to="images/productsbackground/")


class Products(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/products/")

    def __str__(self):
        return self.title
    
    
class ServicesBackgroundImage(models.Model):
    image = models.ImageField(upload_to="images/servicesbackground/")
    
    
class Services(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/services/")

    def __str__(self):
        return self.title


class FeaturesBackgroundImage(models.Model):
    image = models.ImageField(upload_to="images/featuresbackground/")
    
class WarehouseAndLogistic(models.Model):
    image = models.ImageField(upload_to="images/warehouseandlogistic/")
    
    
class Features(models.Model):
    title = models.CharField(max_length=25, default=None)
    description = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.title


class Features_Content(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=30)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    problems = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.doctor.name} - {self.date} - {self.time} - {self.problems}"


class Testimonial(models.Model):
    image = models.ImageField(upload_to="images/testimonial/")
    message = models.TextField(max_length=255)
    patient_name = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)

    def __str__(self):
        return self.patient_name


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class About_Content(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)
admin.site.register(Header)
admin.site.register(Headersocial)
admin.site.register(Carousel)
admin.site.register(Department)
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'department']
    fields = ['name', 'department', 'image', 'facebook_url', 'twitter_url', 'instagram_url']
admin.site.register(CustomizedERP)
admin.site.register(Products)
admin.site.register(Features)
admin.site.register(Appointment)
admin.site.register(Testimonial)
admin.site.register(Subscription)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("service/", service, name="service"),
    path("feature/", feature, name="feature"),
    path("contact/", contact, name="contact"),
    path("submit_newsletter/", submit_newsletter, name="submit_newsletter"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

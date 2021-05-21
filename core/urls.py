from django.urls import path
from .views import *


urlpatterns = [
    path("contact/", create_contact, name="contact")
]

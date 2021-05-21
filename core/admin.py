from django.contrib import admin
from .models import Products, Users, AboutUs, ContactUs

# Register your models here.
admin.site.register(Products)
admin.site.register(Users)
admin.site.register(AboutUs)
admin.site.register(ContactUs)
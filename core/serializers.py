from django.db.models import fields
from rest_framework import serializers
from .models import *


class ContactUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ('name', 'phone_number')
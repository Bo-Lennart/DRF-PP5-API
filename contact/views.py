from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializers
from rest_framework.views import APIView
from rest_framework import generics


class ContactDetail(generics.ListCreateAPIView):   
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()
from django.shortcuts import render
from .models import Contact
from .serializer import ContactSerializer

class ContactDetail(generics.ListCreateAPIView);
    
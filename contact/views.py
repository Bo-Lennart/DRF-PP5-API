from django.shortcuts import render
from .models import Contact
from .serializer import ContactSerializers


class ContactDetail(generics.ListCreateAPIView):   
    serializer_class = ContactSerializers
    queryset = Contact.objects.all()
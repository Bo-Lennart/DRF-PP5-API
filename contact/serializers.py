from rest_framework import serializers
from .models import Contact


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'first_name', 'last_name', 'email_adress', 'message', 'created'
        ]
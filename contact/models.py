from django.db import models


class Contact(models.model):
    first_name: models.Charfield(max_length=50)
    last_name: models.Charfield(max_length=50)
    email_adress: models.Charfield(max_length=50)
    message: models.Charfield(max_length=50)
    created: models.DateTimeField(auto_now_add=True)

    
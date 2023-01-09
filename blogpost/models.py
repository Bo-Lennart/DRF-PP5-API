
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class BlogPost(models.Model):
    CATEGORY_CHOICE = [
        ('WORLD', 'World'),
        ('BUSINESS', 'Business'),
        ('FOOD', 'Food'),
        ('CULTURE', 'Culture'),
        ('MUSIC', 'Music'),
        ('TECH', 'Tech')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_dyyoey', blank=True
    )
    category = models.CharField(
        max_length=8, choices=CATEGORY_CHOICE, default='WORLD'
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.id} {self.title}"
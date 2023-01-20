from django.db import models
from django.contrib.auth.models import User
from blogpost.models import BlogPost


class Bookmark(models.Model):
    """
    Bookmark model, for 'owner' and 'post'.
    'unique_together' = a user can't bookmark the same post several time.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        BlogPost,
        related_name='bookmark',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'

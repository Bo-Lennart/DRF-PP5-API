from django.db import models
from django.contrib.auth.models import User
from blogpost.models import BlogPost


class Like(models.Model):
    """
    Like model, for 'owner' and 'post'.
    'unique_together' = a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        BlogPost,
        related_name='likes',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'

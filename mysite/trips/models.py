from django.db import models
from accounts.models import UserProfile

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
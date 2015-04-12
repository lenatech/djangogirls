from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
        # This line is required. Links UserProfile to a User model instance.
        user = models.OneToOneField(User)
        # The additional attributes we wish to include.
        website = models.URLField(blank=True)
        avatar = models.ImageField(
            upload_to='images/avatar',
            default = 'images/avatar/default.jpg', 
            blank=True)

        # Override the __unicode__() method to return out something meaningful!
        def __unicode__(self):
            return self.user.username

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    biography = models.TextField()
    image = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
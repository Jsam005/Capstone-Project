from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField(blank=True)
    biography = models.TextField(blank=True, help_text='Tell us about yourself')
    profile_image = models.ImageField(upload_to='profile_images', blank=True, default='/static/images/default-profile.png')

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)
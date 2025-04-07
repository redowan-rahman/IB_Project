from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    about = models.TextField(blank=True)
    job = models.CharField(max_length=150, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
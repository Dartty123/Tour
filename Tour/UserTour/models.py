from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="details")
    phone_number = models.CharField(max_length=18, null=True, default=None)
    bio = models.TextField(null=True, default=None)
    avatar = models.ImageField(upload_to="-", null=True, default=None)

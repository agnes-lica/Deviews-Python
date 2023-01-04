from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(max_length=255)
    profile_picture = models.CharField()
    is_active = models.BooleanField(default=True)
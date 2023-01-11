from django.contrib.auth.models import AbstractUser
from django.db import models
from techs.models import Tech


class User(AbstractUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(max_length=255, null=True)
    profile_picture = models.URLField(
        default="https://cdn-icons-png.flaticon.com/512/149/149071.png",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    techs = models.ManyToManyField(Tech, related_name="users")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

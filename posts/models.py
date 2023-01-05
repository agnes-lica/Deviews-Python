from django.db import models


class Post(models.Model):
    content = models.TextField()
    post_picture = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = ...
    techs = ...

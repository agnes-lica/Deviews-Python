from django.db import models


class Post(models.Model):
    class Meta:
        ordering = ["id"]

    content = models.TextField()
    post_picture = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = ...
    techs = ...

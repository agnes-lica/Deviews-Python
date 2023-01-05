from django.db import models

class FirePost(models.Model):
    exists = models.BooleanField(null=True, default=True)
    # user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="fires", null=True)
    # post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="fires", null=True)

class FireComments(models.Model):
    ...
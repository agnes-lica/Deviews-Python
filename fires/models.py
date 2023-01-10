from django.db import models

class FirePost(models.Model):
    exists = models.BooleanField(null=True, default=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="fires")
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="fires")

class FireComments(models.Model):
    exists = models.BooleanField(null=True, default=True)
    # user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="fires", null=True)
    # comment = models.ForeignKey("comments.Comment", on_delete=models.CASCADE, related_name="fires", null=True)
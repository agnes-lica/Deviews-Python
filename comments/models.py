from django.db import models


class Comment(models.Model):
    class Meta:
        ordering = ["id"]

    content = models.CharField(max_length=255)  # , blank=False, null=False
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="comments")


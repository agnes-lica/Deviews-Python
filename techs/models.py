from django.db import models


class Tech(models.Model):
    class Meta:
        ordering = ["id"]
    tech_name = models.CharField(max_length=100 ,null=False)

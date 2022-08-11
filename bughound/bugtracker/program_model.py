from django.db import models
from .area_model import Area


class Program(models.Model):
    name = models.TextField(unique=True, null=False, blank=False)
    release = models.TextField()
    version = models.TextField()
    area = models.ForeignKey(Area, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

class link(models.Model):
    original = models.URLField(unique=True)
    shortened = models.CharField(max_length=8)

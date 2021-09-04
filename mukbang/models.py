from django.db import models


# Create your models here.
class Muckbang(models.Model):
    group = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    tag = models.CharField(max_length=20)
    link = models.TextField()
    description = models.TextField()
    image = models.ImageField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
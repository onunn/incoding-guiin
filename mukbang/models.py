from django.db import models


# Create your models here.


class Group(models.Model):
    group_classifier = models.CharField(max_length=2)
    description = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Muckbang(models.Model):
    group = models.ForeignKey(Group, on_delete= models.CASCADE)
    name = models.CharField(max_length=20)
    tag = models.CharField(max_length=20)
    link = models.TextField()
    image = models.ImageField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
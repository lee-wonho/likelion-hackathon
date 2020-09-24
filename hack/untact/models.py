from django.db import models

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=30)

class Info(models.Model):
    category= models.CharField(max_length=20)
    startdate=models.DateField()
    enddate=models.DateField()
    href = models.URLField()
    img =models.URLField()
    title=models.CharField(max_length=100)
    actor=models.CharField(max_length=100)

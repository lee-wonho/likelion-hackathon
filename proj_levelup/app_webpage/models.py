from django.db import models

# Create your models here.
class Category(models.Model):
    category_num = models.IntegerField()
    category = models.CharField(max_length=20)

class Good(models.Model):
    enddate = models.DateTimeField
    startdate = models.DateTimeField
    href = models.TextField()
    img = models.TextField()
    title = models.TextField()
    players = models.TextField()
    category = models.IntegerField()
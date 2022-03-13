from django.db import models

# Create your models here.

class Words(models.Model):
    word = models.CharField(max_length=5,default="")
    date = models.DateField()
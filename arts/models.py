from cgitb import text
from statistics import mode
from turtle import heading
from django.db import models

# Create your models here.
class Image(models.Model):
    heading = models.CharField(max_length=15)
    maintext = models.CharField(max_length=20)
    image = models.ImageField(null = True )
    
class photo(models.Model):
    heading = models.CharField(max_length=15)
    maintext = models.CharField(max_length=20)
    image = models.ImageField(null =True )
    
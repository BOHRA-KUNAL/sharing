from django.db import models
from . models import *

# Create your models here.

class courses(models.Model):
    name=models.CharField(max_length = 100)
    img=models.ImageField(null=True,blank=True)
    price=models.IntegerField()
    desc=models.CharField(max_length = 3000)


class blogs(models.Model):
    name=models.CharField(max_length = 100)
    img=models.ImageField(null=True,blank=True)
    desc=models.CharField(max_length = 3000)


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name
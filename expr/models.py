from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=16)
    lname = models.CharField(max_length=16)
    email = models.EmailField(max_length=244)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
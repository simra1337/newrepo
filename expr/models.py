from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=16, blank=False, null=False)
    lname = models.CharField(max_length=16, blank=False, null=False)
    email = models.EmailField(max_length=244, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=False, null=False)
    password = models.CharField(max_length=32, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class User(models.Model):
    name = models.TextField()
    # class

class Class(models.Model):
    # code
    # timer
    # name
    # personnel
    created_at = models.DateTimeField(auto_now_add=True)
    
class Role(models.Model):
    # class
    # user
    is_ckecker = models.BooleanField(default=False)

class Attendance(models.Model):
    # class
    # user
    is_attendance = models.BooleanField(default=False)
    checked_at = models.DateTimeField(auto_now_add=True)
'''
User-----------------------
sttings.AUTH_USER_MODEL
-----------------------

-----------------------

-----------------------

'''
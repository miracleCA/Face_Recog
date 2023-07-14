from django.db import models
from django.contrib.auth.models import *
from django.db.models.signals import post_save

class UserProfile(models.Model):
    face_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length = 30)
    phone = models.CharField(max_length =  15)
    department = models.CharField(max_length = 50, default="")
    occupation = models.CharField(max_length = 30, default="")
    job = models.CharField(max_length = 50)
    bio = models.TextField(max_length = 200)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.firstname
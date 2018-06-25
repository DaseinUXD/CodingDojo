from django.db import models
import re

# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(models.Model):
    name = models.CharField(max_length=255),
    alias = models.CharField(max_length=255),
    email = models.CharField(max_length=255),
    password = models.CharField(max_length=255),

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.login


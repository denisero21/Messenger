from django.conf import settings
from django.db import models
from django.utils import timezone


class user(models.Model):
    email = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    bio = models.TextField()

    def register():
        pass

    def auth():
        pass

    def __str__(self):
        return self.login


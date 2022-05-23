from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.login

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(user, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)


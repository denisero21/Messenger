
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid
from django.urls import reverse

class Room(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.CASCADE)
    deliver = models.ForeignKey(User, related_name='deliver', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    slug = models.SlugField(unique=True, default=uuid.uuid4)

    def __str__(self):
        return str(self.id)
    
    


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
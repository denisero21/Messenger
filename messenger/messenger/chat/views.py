from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Room
from django.db.models import Q
from itertools import chain

@login_required
def room(request, id):
    room = Room.objects.get(id=id)
    messages = Message.objects.filter(room=room)[0:50]
    # rooms = Room.objects.filter(Q(sender=request.user) | Q(deliver=request.user))
    rooms = Room.objects.filter(Q(sender=request.user) | Q(deliver=request.user))
    return render(request, 'chat.html', {'room': room, 'messages': messages, 'rooms': rooms})
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Room

@login_required
def main(request):
    rooms = Room.objects.all()
    return render(request, 'main.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:50]
    return render(request, 'chat.html', {'room': room, 'messages': messages})
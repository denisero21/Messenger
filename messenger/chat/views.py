import logging
from urllib import request
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Message, Room
from django.db.models import Q
from itertools import chain
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth import login
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

logger = logging.getLogger('django')

@login_required
def main(request):
    rooms = Room.objects.filter(Q(sender=request.user) | Q(deliver=request.user))
    users = User.objects.all()
    return render(request, 'main.html', {'rooms': rooms,'users': users})

@login_required
def room(request, id):
    room = Room.objects.get(id=id)
    messages = Message.objects.filter(room=room)[0:50]
    rooms = Room.objects.filter(Q(sender=request.user) | Q(deliver=request.user))
    return render(request, 'chat.html', {'room': room, 'messages': messages, 'rooms': rooms})

@login_required
def search(request):
    users = User.objects.all()
    rooms = Room.objects.filter(Q(sender=request.user) | Q(deliver=request.user))
    return render(request, "search.html", {'users': users, 'rooms': rooms,})

@login_required
def profile(request):
    rooms = Room.objects.filter(Q(sender=request.user) | Q(deliver=request.user))
    return render(request, 'profile.html', {'rooms': rooms})


class UserList(ListView):
    model = User
    context_object_name = 'usernames'
    template_name = 'search.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     search_input = self.request.GET.get('search-area')
    #     if search_input:
    #         context['username'] = context['username'].filter(username__icontains=search_input)

    #     return context
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context = Room.objects.filter(Q(sender=self.request.user) | Q(deliver=self.request.user))
        return {'rooms': context}

    def get_queryset(self):
        search_in = self.request.GET.get('search-area') 
        return User.objects.filter(username__icontains=search_in)


class RoomCreate(LoginRequiredMixin, CreateView):
    model = Room
    fields = ['sender', 'deliver', 'name'] 
    success_url = reverse_lazy(main)
    
    def get_context_data(self, **kwargs):
            context =  super().get_context_data(**kwargs)
            context = Room.objects.filter(Q(sender=self.request.user) | Q(deliver=self.request.user))
            users = User.objects.all()
            return {'rooms': context, 'users': users}

    def form_valid(self, form):
        logger.info("Chat was created")
        return super(RoomCreate, self).form_valid(form)
    


class RoomDelete(DeleteView):
    model = Room
    context_object_name = 'room'
    success_url = reverse_lazy(main)
    logger.info('Chat was deleted')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context = Room.objects.filter(Q(sender=self.request.user) | Q(deliver=self.request.user))
        return {'rooms': context}


def delete_user(request):    
    u = User.objects.get(username = request.user.username)
    u.delete()
    logger.info('The user was deleted')
    return redirect('')

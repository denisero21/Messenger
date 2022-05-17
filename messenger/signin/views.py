from django.shortcuts import render
from distutils.log import Log
from re import template
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import *
  
def index(request):
    return render(request, "index.html")
 
def auth(request):
    return render(request, "auth/auth.html")
 
def register(request):
    return render(request, "register/register.html")

def main(requset):
    users = user.objects.all
    return render(requset, "main.html", {'users': users})

class CustomLoginView(LoginView):
    template_name = '../templates/auth/auth.html'
    filed = '__all__'   
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')

def chat(request):
    users = user.objects.all
    return render(request, 'chat.html', {'users': users})
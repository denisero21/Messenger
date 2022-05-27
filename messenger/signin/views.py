import logging
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.shortcuts import render
from django.contrib.auth import login

logger = logging.getLogger('django')

def index(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        return render(request, "index.html")

class CustomLoginView(LoginView):
    template_name = '../templates/auth/auth.html'
    filed = '__all__'   
    redirect_authenticated_user = True

    def get_success_url(self):
        logger.info('The user succesfully loged in')
        return reverse_lazy('main')
        

class RegisterView(FormView):
    template_name = '../templates/register/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        logger.info('The user was registrated succesfully')
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super(RegisterView, self).get(*args, **kwargs)






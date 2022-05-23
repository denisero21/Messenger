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
from chat.models import Room
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q

def index(request):
     # if request.user.is_authenticated:
     #     HttpResponseRedirect(reverse('main'))
     # else:
    return render(request, "index.html")
         # return None

class CustomLoginView(LoginView):
    template_name = '../templates/auth/auth.html'
    filed = '__all__'   
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')
        

class RegisterView(FormView):
    template_name = '../templates/register/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super(RegisterView, self).get(*args, **kwargs)


@login_required
def main(request):
    rooms = Room.objects.filter(Q(sender=request.user) | Q(deliver=request.user))
    users = User.objects.all()
    return render(request, 'main.html', {'rooms': rooms, 'users': users})


class UserList(ListView):
    model = User
    context_object_name = 'usernames'
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area')
        if search_input:
            context['username'] = context['username'].filter(username__icontains=search_input)

        return context

    def get_queryset(self):
        search_in = self.request.GET.get('search-area') 
        return User.objects.filter(username__icontains=search_in)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['username'] = context['username'].filter(user=self.request.user)

    #     search_input = self.request.GET.get('search-area') or ''
    #     if search_input:
    #         context['username'] = context['username'].filter(username__icontains=search_input)

    #     context['search_input'] = search_input
    #     return context

def search(request):
    users = User.objects.all()
    rooms = Room.objects.filter(Q(sender=request.user) | Q(deliver=request.user))
    return render(request, "search.html", {'users': users, 'rooms': rooms})



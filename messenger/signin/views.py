from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.shortcuts import render
from django.contrib.auth import login
from chat.models import Room
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

def index(request):
    return render(request, "index.html")

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
    rooms = Room.objects.all()
    return render(request, 'main.html', {'rooms': rooms})


@login_required
def room(request, slug):
    rooms = Room.objects.all()
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:50]
    return render(request, 'chat.html', {'rooms': rooms, 'room': room, 'messages': messages})

class UserList(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login'] = context['login'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['login'] = context['login'].filter(title__icontains=search_input)

        context['search_input'] = search_input
        return context

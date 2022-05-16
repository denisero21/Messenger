from django.shortcuts import render

from django.http import HttpResponse
  
def index(request):
    return render(request, "index.html")
 
def auth(request):
    return render(request, "auth/auth.html")
 
def contact(request):
    return HttpResponse("<h2>Контакты</h2>")
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('auth/', CustomLoginView.as_view(), name='auth'),
    path('auth/', views.auth),
    path('register/', views.register),
    path('main/', views.main, name='main'),
    path('chatc/', views.chat),
]
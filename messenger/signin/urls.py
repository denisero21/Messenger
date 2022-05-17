from django.urls import path
from .views import index, CustomLoginView, register, main, auth, chat

urlpatterns = [
    path('', index),
    # path('auth/', CustomLoginView.as_view(), name='auth'),
    path('auth/', auth),
    path('register/', register),
    path('main/', main, name='main'),
    path('chat/', chat)
]
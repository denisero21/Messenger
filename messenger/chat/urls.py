from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('profile/delete/', views.delete_user, name='delete_user'),
    path('send/', views.RoomCreate.as_view(), name='send'),
    path('<slug:id>/', views.room, name='room'),
    path('delete_room/<slug:slug>/', views.RoomDelete.as_view(), name='delete_room')
]
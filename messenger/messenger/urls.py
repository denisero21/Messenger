from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('signin.urls'))
    # path('', views.index),
    # path('auth/', views.auth),
    # path('register/', views.register),
    # path('main/', views.main)
]

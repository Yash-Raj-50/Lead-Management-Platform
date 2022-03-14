from django.contrib import admin
from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', views.index, name='authentication'),
    path('register', views.register, name='registration'),
    path('login', views.index, name='authentication'),
    path('signin', views.signin, name='signin'),
]

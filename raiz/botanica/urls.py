#se puede quitar htmls y solo usar uno para todos los demas 
#solo que todos los demas no se pasan a django.

from django.contrib import admin
from django.urls import path,include
from .views import index,home,borgona

urlpatterns = [
    path('index',index,name="index"),
    path('home',home,name="home"),
    path('',borgona,name="borgona"),
]
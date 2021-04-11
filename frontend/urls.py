from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('join', views.index, name='join'),
    path('create', views.index, name='create'),

]

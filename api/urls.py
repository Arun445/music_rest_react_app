from django.urls import path, include
from . import views



urlpatterns =[
    path('room', views.RoomView.as_view(), name='view' ),
    path('create-room', views.CreateRoomView.as_view(), name='create_view' ),


]
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name = "home"),
    path('register/',register,name = 'register'),
    path('login/',login,name = 'login'),
    path('switch/',log2,name = 'log2'),
    path('greeting/<int:face_id>/',Greeting,name='greeting'),
]

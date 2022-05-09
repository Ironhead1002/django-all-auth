from django.contrib import admin
from .views import welcome
from django.urls import path, include

urlpatterns = [
    path('', welcome, name="welcome"),
]

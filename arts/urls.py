from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path('',views.index,name="index"),
   path('addyour',views.addyour,name="addyour")
]

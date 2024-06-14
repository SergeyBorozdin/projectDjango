from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('add_register', views.add_register),
    path('delete_register', views.delete_register),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='register'),
    path('about', views.about, name='about'),
    path('add_register', views.add_register, name='add_register'),
    path('delete_register', views.delete_register, name='delete_register'),
]

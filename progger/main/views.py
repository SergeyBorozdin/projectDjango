from django.shortcuts import render
from .models import Equipment


# Create your views here.

def index(request):
    register = Equipment.objects.order_by('-date')
    return render(request, 'main/index.html', {'register': register})


def about(request):
    return render(request, 'main/about.html')


def add_register(request):
    return render(request, 'main/add_register.html')


def delete_register(request):
    return render(request, 'main/delete_register.html')

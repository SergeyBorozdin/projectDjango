from django.shortcuts import render
from .models import Equipment
from .forms import EquipmentForm


# Create your views here.

def index(request):
    register = Equipment.objects.all()
    return render(request, 'main/index.html', {'register': register})


def add_register(request):
    form = EquipmentForm()

    data = {
        'form' : form
    }

    return render(request, 'main/add_register.html', data)


def delete_register(request):
    return render(request, 'main/delete_register.html')


def about(request):
    return render(request, 'main/about.html')



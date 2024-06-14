from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def add_register(request):
    return render(request, 'main/add_register.html')


def delete_register(request):
    return render(request, 'main/delete_register.html')

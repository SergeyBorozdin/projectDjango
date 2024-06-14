from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<h4> test work <h4>')


def about(request):
    return HttpResponse('<h2> about test work <h2>')


def register(request):
    return HttpResponse('<h2> register test work <h2>')

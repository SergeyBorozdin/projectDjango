from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentForm
from django.views.generic import DetailView, UpdateView, DeleteView

from django.contrib.auth import login, authenticate
from .forms import RegisterForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@login_required
def add_register(request):
    error = ''
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            error = 'Форма была не верной'
    form = EquipmentForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_register.html', data)

@login_required
def edit_register(request):
    register = Equipment.objects.all()
    return render(request, 'main/edit_register.html', {'register': register})

@login_required
def delete_register(request):
    register = Equipment.objects.all()
    return render(request, 'main/delete_register.html', {'register': register})

@method_decorator(login_required, name='dispatch')
class RegisterRecordView(DetailView):
    model = Equipment
    template_name = 'main/detail_view.html'
    context_object_name = 'equipment'


@method_decorator(login_required, name='dispatch')
class RegisterRecordUpdate(UpdateView):
    model = Equipment
    template_name = 'main/add_register.html'
    form_class = EquipmentForm

@method_decorator(login_required, name='dispatch')
class RegisterRecordDelete(DeleteView):
    model = Equipment
    success_url = '/edit_register'
    template_name = 'main/delete_record.html'

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'main/registration/registration.html', {'form': form})


def index(request):
    register = Equipment.objects.all()
    return render(request, 'main/index.html', {'register': register})


class RegisterRecordView(DetailView):
    model = Equipment
    template_name = 'main/detail_view.html'
    context_object_name = 'equipment'


class RegisterRecordUpdate(UpdateView):
    model = Equipment
    template_name = 'main/add_register.html'

    form_class = EquipmentForm


class RegisterRecordDelete(DeleteView):
    model = Equipment
    success_url = '/edit_register'
    template_name = 'main/delete_record.html'


def add_register(request):
    error = ''
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            error = 'Форма была не верной'
    form = EquipmentForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_register.html', data)


def edit_register(request):
    register = Equipment.objects.all()
    return render(request, 'main/edit_register.html', {'register': register})


def about(request):
    return render(request, 'main/about.html')

from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.

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

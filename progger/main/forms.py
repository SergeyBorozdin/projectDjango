from .models import Equipment
from django.forms import ModelForm, TextInput, DateInput, FileInput, NumberInput

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['title', 'article', 'lm_article', 'length',
                  'width', 'depth', 'shop', 'amount', 'address', 'image', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            "article": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Артикул'
            }),
            "lm_article": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Артикул ЛМ'
            }),
            "length": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Длина'
            }),
            "width": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ширина'
            }),
            "depth": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Высота'
            }),
            "shop": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Магазин'
            }),
            "amount": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес хранения'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фото'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата',
                'type': 'date'  # HTML5 date input
            })
        }

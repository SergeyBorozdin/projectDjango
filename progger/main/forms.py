from .models import Equipment
from django.forms import ModelForm, TextInput, DateInput, FileInput, NumberInput



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


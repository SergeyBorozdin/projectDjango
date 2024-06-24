from .models import Equipment
from django.forms import ModelForm, TextInput, DateInput, FileInput



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
            "length": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Длина'
            }),
            "width": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ширина'
            }),
            "depth": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Длина'
            }),
            "shop": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Магазин'
            }),
            "amount": TextInput(attrs={
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
                'placeholder': 'Дата'
            })
        }


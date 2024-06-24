from .models import Equipment
from django.forms import ModelForm, TextInput, DateInput, IntegerField, FileInput



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
            "length": IntegerField(attrs={
                'class': 'form-control',
                'placeholder': 'Длина'
            }),
            "width": IntegerField(attrs={
                'class': 'form-control',
                'placeholder': 'Ширина'
            }),
            "depth": IntegerField(attrs={
                'class': 'form-control',
                'placeholder': 'Длина'
            }),
            "shop": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Магазин'
            }),
            "amount": IntegerField(attrs={
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
                'placeholder': 'Фото'
            })
        }


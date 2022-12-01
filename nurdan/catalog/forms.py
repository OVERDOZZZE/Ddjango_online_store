from .models import Catalog
from django.forms import ModelForm, TextInput, NumberInput, Textarea


class CatalogForm(ModelForm):
    class Meta:
        model = Catalog
        fields = ['title', 'description', 'price']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена'
            })

        }




















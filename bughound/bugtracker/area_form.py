from django.forms import ModelForm
from django import forms

from .area_model import Area


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'program']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'program': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Program'})
        }
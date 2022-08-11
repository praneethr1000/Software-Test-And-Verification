from django.forms import ModelForm
from django import forms

from .area_model import Area


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['name']

        widgets = {
            'name': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Name'}),
        }
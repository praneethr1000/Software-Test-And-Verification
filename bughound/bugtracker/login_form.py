from django.forms import ModelForm
from django import forms

from .login_model import Login


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
        }
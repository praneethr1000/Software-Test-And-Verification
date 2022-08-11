from django.forms import ModelForm
from django import forms

from .employee_model import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'loginID', 'level']

        widgets = {
            'user': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'User'}),
            'loginID': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'LoginID'}),
            'level': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Level'})
        }
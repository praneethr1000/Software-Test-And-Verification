from django import forms
from django.forms import ModelForm
from .models import Bugtracker


class BugReportForm(ModelForm):
    class Meta:
        model = Bugtracker

        fields = ['program', 'report_type', 'severity', 'problem_summary', 'reported_by', 'date']

        widgets = {
            'program': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Program'}),
            'report_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Report Type'}),
            'severity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Severity'}),
            'problem_summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Problem Summary'}),
            'reported_by': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Reported By'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        }

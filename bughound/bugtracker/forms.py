from django import forms
from django.forms import ModelForm
from .models import Bugtracker


class BugReportForm(ModelForm):
    class Meta:
        model = Bugtracker

        # TODO: 2. Update the new field here
        fields = ['program', 'report_type', 'severity', 'problem_summary','problem', 'suggested_fix', 'reproducible',
                  'functional_area', 'assigned_to', 'comments', 'status', 'priority', 'resolution', 'resolution_version',
                  'resolved_by', 'resolved_date', 'tested_by', 'tested_date', 'treated_as_deferred', 'reported_by', 'date']

        widgets = {
            'program': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Program'}),
            'report_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Report Type'}),
            'severity': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Severity'}),
            'problem_summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Problem Summary'}),
            # TODO: 3. Update the new field here
            'problem': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Problem'}),
            'suggested_fix': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Suggested Fix'}),
            'reproducible': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reproducible (Y/N)'}),
            'functional_area' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Functional Area'}),
            'assigned_to' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assigned To'}),
            'comments' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comments'}),
            'status' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}),
            'priority' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Priority'}),
            'resolution' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Resolution'}),
            'resolution_version' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Resolution Version'}),
            'resolved_by' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Resolved By'}),
            'resolved_date' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Resolved Date'}),
            'tested_by' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Tested By'}),
            'tested_date' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tested Date'}),
            'treated_as_deferred' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Deferred (Y/N)'}),
            'reported_by': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Reported By'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
        }

import django_filters
from .models import *


class BugFilter(django_filters.FilterSet):
    class Meta:
        model = Bugtracker
        fields = '__all__'
        exclude = ['problem_summary', 'date']

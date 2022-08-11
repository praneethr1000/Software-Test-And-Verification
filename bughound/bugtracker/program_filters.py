import django_filters
from .program_model import *


class ProgramFilter(django_filters.FilterSet):
    class Meta:
        model = Program
        fields = '__all__'
        exclude = ['area']

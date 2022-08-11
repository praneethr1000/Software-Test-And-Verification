import django_filters
from .area_model import *


class AreaFilter(django_filters.FilterSet):
    class Meta:
        model = Area
        fields = '__all__'

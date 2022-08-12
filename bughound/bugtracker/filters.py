import django_filters

from .models import *


class BugFilter(django_filters.FilterSet):

    class Meta:
        model = Bugtracker
        fields = '__all__'
        exclude = ['problem_summary', 'problem', 'suggested_fix',
                   'reproducible', 'comments', 'resolution_version',
                   'resolved_date', 'tested_by', 'tested_date', 'treated_as_deferred', 'attachment']

    def __init__(self, *args, **kwargs):
        super(BugFilter, self).__init__(*args, **kwargs)
        self.form.initial['status'] = 'Open'

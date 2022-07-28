from import_export import resources
from .models import Bugtracker


class BugResource(resources.ModelResource):
    class Meta:
        model = Bugtracker

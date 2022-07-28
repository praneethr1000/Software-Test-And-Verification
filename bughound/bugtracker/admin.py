from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
from .models import Bugtracker

# admin.site.register(Bugtracker)


class BugResource(resources.ModelResource):
    class Meta:
        model = Bugtracker


class BugAdmin(ImportExportModelAdmin):
    resource_class = BugResource


admin.site.register(Bugtracker, BugAdmin)

from django.contrib import admin
from django_reverse_admin import ReverseModelAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .program_model import Program
from .area_model import Area
from django import forms

# Register your models here.
from .models import Bugtracker


# admin.site.register(Bugtracker)


class BugResource(resources.ModelResource):
    class Meta:
        model = Bugtracker


class BugReverseAdmin(ReverseModelAdmin, ImportExportModelAdmin):
    resource_class = BugResource
    inline_type = 'tabular'
    inline_reverse = [('program', {'fields': ['name', 'release', 'version']})]


class ProgramResource(resources.ModelResource):
    class Meta:
        model = Program


class ProgramAdmin(ImportExportModelAdmin):
    resource_class = ProgramResource


class AreaResource(resources.ModelResource):
    class Meta:
        model = Area


class AreaAdmin(ImportExportModelAdmin):
    resource_class = AreaResource


admin.site.register(Bugtracker, BugReverseAdmin)
# admin.site.register(Bugtracker, BugAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Area, AreaAdmin)

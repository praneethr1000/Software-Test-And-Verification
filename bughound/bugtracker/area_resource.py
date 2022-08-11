from import_export import resources

from .area_model import Area


class AreaResource(resources.ModelResource):
    class Meta:
        model = Area
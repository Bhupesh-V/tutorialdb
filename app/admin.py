from django.contrib import admin

# Register your models here.
from . models import tutorial, tag
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget

admin.site.register(tag)

class TutorialResource(resources.ModelResource):
    tags = fields.Field(
        column_name='tags',
        attribute='tags',
        widget=ManyToManyWidget(tag, ',', 'name'))
    class Meta:
        model = tutorial
        exclude = ('id',)
        export_order = ('title', 'link', 'tags', 'category', 'created_date')
        import_id_fields = ('title', 'link')


@admin.register(tutorial)
class TutorialAdmin(ImportExportModelAdmin):
	resource_class = TutorialResource
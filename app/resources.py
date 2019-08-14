from import_export import resources, fields
from . models import tutorial, tag
from import_export.widgets import ManyToManyWidget


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


class TagResource(resources.ModelResource):
    class Meta:
    	model = tag
    	exclude = ('id',)
    	export_order = ('name', 'description', 'created_date')
    	import_id_fields = ('name', 'description')
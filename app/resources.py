from import_export import fields, resources
from import_export.widgets import ManyToManyWidget
from . models import Tutorial, Tag


class TutorialResource(resources.ModelResource):
    tags = fields.Field(
        column_name='tags',
        attribute='tags',
        widget=ManyToManyWidget(Tag, ',', 'name'))

    class Meta:
        model = Tutorial
        exclude = ('id',)
        export_order = ('title', 'link', 'tags', 'category', 'created_date', 'publish')
        import_id_fields = ('title', 'link')


class TagResource(resources.ModelResource):

    class Meta:
        model = Tag
        exclude = ('id',)
        export_order = ('name', 'description', 'created_date')
        import_id_fields = ('name', 'description')

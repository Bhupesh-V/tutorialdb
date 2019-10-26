from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Tag, Tutorial
from .resources import TagResource, TutorialResource

@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource


@admin.register(Tutorial)
class TutorialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'title', 'publish')
    resource_class = TutorialResource
    actions = ['publish_tutorial']

    def publish_tutorial(self, request, queryset):
        rows_updated = queryset.update(publish=True)

        if rows_updated == 1:
            message_bit = '1 Tutorial was'
        else:
            message_bit = f'{rows_updated} Tutorials were'
        self.message_user(request, f'{message_bit} marked as published.')

    publish_tutorial.short_description = 'Publish selected tutorials'

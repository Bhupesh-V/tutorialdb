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

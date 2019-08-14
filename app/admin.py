from django.contrib import admin
from . models import tutorial, tag
from import_export.admin import ImportExportModelAdmin
from  . resources import TagResource, TutorialResource


@admin.register(tutorial)
class TutorialAdmin(ImportExportModelAdmin):
	resource_class = TutorialResource

@admin.register(tag)
class TagAdmin(ImportExportModelAdmin):
	resource_class = TagResource
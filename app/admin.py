from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Tutorial, Tag
from  .resources import TutorialResource, TagResource

@admin.register(Tutorial)
class TutorialAdmin(ImportExportModelAdmin):
    resource_class = TutorialResource

@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource

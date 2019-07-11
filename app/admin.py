from django.contrib import admin

# Register your models here.
from . models import tutorial, tag

admin.site.register(tag)
admin.site.register(tutorial)
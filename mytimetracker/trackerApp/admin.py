from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.HighLevelTask)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'task_type', 'status', 'publish')
    list_filter = ('status', 'created', 'publish', 'task_type')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.HighLevelTask)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'task_type', 'publish')
    list_filter = ('created', 'publish', 'task_type')
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ('publish', )


@admin.register(models.LowLevelTask)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'publish')
    list_filter = ('created', 'publish', 'status')
    search_fields = ('title', )
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ('publish', )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created',)
    list_filter = ('created',)
    search_fields = ('name', 'body')

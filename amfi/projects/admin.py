from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class ProjectAdmin(SummernoteModelAdmin):
    list_display = ['title', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    summernote_fields = ('body', 'sub_body2',)
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(Project, ProjectAdmin)
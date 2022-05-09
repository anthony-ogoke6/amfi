from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class AboutAdmin(SummernoteModelAdmin):
    list_display = ['title', 'slug', 'author', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    summernote_fields = ('body', 'sub_body', 'sub_body2', 'sub_body3',)
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(About, AboutAdmin)
from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class AboutAdmin(SummernoteModelAdmin):
    list_display = ['title', 'slug', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    summernote_fields = ('body', 'sub_body',)
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(About, AboutAdmin)
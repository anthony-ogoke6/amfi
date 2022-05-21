from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class NewsAdmin(SummernoteModelAdmin):
    list_display = ['title', 'author', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    summernote_fields = ('body', 'body_2', 'quote',)
    #prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(News, NewsAdmin)
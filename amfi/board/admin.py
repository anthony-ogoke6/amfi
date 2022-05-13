from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class BoardAdmin(SummernoteModelAdmin):
    list_display = ['full_name', 'designation', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    summernote_fields = ('speech',)
    prepopulated_fields = {'slug':('full_name',)}
    list_editable = ('status',)
    date_hierarchy = ('created')





admin.site.register(Board, BoardAdmin)


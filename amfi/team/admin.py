from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class TeamAdmin(SummernoteModelAdmin):
    list_display = ['full_name', 'designation', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    list_editable = ('status',)
    date_hierarchy = ('created')





admin.site.register(Team, TeamAdmin)

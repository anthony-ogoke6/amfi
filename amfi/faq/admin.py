from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class FaqAdmin(SummernoteModelAdmin):
    list_display = ['category', 'question', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    summernote_fields = ('answer',)
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(Faq, FaqAdmin)
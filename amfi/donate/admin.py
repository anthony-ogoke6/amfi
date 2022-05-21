from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin




class DonateAdmin(SummernoteModelAdmin):
    list_display = ['title',  'created', 'updated']
    list_filter = ('created', 'updated')
    summernote_fields = ('fees',)
    date_hierarchy = ('created')


admin.site.register(Donate, DonateAdmin)


# Register your models here.

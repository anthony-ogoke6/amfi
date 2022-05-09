from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class ContactAdmin(SummernoteModelAdmin):
    list_display = ['title', 'slug', 'author', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    summernote_fields = ('description',)
    prepopulated_fields = {'slug':('title',)}
    list_editable = ('status',)
    date_hierarchy = ('created')



class ContactMessageAdmin(SummernoteModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'subject', 'created', 'updated']
    list_filter = ('created', 'updated')
    summernote_fields = ('message',)
    prepopulated_fields = {'slug':('subject',)}
    date_hierarchy = ('created')


admin.site.register(ContactMessage, ContactMessageAdmin)

admin.site.register(Contact, ContactAdmin)
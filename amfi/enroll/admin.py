from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin




class EnrollAdmin(SummernoteModelAdmin):
    list_display = ['full_name', 'email', 'phone_number', 'training', 'payment_status', 'created', 'updated']
    list_filter = ('created', 'updated')
    summernote_fields = ('address', 'enter_your_parish',)
    date_hierarchy = ('created')


admin.site.register(Enroll, EnrollAdmin)


# Register your models here.

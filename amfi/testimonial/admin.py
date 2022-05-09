from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin



class TestimonialAdmin(SummernoteModelAdmin):
    list_display = ['full_name', 'designation', 'rating', 'status', 'created', 'updated']
    list_filter = ('status', 'created', 'updated')
    summernote_fields = ('testimony',)
    list_editable = ('status',)
    date_hierarchy = ('created')


admin.site.register(Testimonial, TestimonialAdmin)
from __future__ import unicode_literals

from django.db import models
from authentication.models import User
import uuid
from django.urls import reverse
from django.db.models.fields import BLANK_CHOICE_DASH
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.core.mail import send_mail
from django.conf import settings
from tinymce import models as tinymce_models
# Create your models here.



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")




class Testimonial(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    status                  =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    full_name    =      models.CharField(max_length=400)
    designation   =      models.CharField(max_length=200)
    image_50_by_50               =       models.ImageField(blank=True, null=True)
    testimony    =      models.TextField(blank=True, null=True)
    rating          =       models.PositiveIntegerField(default=0)
    
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)

    class Meta:
    	verbose_name = 'Testimonial'
    	verbose_name_plural = 'Testimonials'

    def __str__(self):
    	return self.full_name


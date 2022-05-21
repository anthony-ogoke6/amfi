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





class Contact(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    status              =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    title               =       models.CharField(max_length=200, blank=True, null=True)
    description         =       models.TextField(blank=True, null=True)
    email               =       models.EmailField(blank=True, null=True)
    location            =       models.CharField(max_length=200, blank=True, null=True)
    support_line        =       models.CharField(max_length=200, blank=True, null=True)
    
    view_count          =       models.PositiveIntegerField(default=0)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-id']
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Contact)
def pre_save_slug1(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug




# Create your models here.
class ContactMessage(models.Model):

    full_name    =      models.CharField(max_length=400)
    email   =      models.EmailField(blank=False, null=False)
    phone_number    =      models.CharField(max_length=200, blank=True, null=True)
    subject   =      models.CharField(max_length=200, blank=True, null=True)
    message      =       models.TextField(blank=True, null=True)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return self.full_name
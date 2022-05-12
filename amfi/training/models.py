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





class Training(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    category               	=       models.CharField(max_length=200, blank=True, null=True)
    title               	=       models.CharField(max_length=400, blank=True, null=True)
    slug                	=       models.SlugField(max_length=200, blank=True, null=True)
    location                =       models.CharField(max_length=200, blank=True, null=True)
    facilitator              =       models.CharField(max_length=200, blank=True, null=True)
    image_570_by_640    	=       models.ImageField(blank=True, null=True)
    sub_title               =       models.CharField(max_length=200, blank=True, null=True)
    body                	=       models.TextField(blank=True, null=True)
    image_770_by_445        =       models.ImageField(blank=True, null=True)
    sub_title2               =       models.CharField(max_length=200, blank=True, null=True)
    sub_body2               =       models.TextField(blank=True, null=True)
    status              	=       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    view_count          	=       models.PositiveIntegerField(default=0)
    created             	=       models.DateTimeField(auto_now_add=True)
    updated             	=       models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-id']
        verbose_name = 'Training'
        verbose_name_plural = 'Training'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("training:training_details", args=[self.id, self.slug])


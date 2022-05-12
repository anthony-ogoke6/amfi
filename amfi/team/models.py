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




class Team(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    status              =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    full_name           =       models.CharField(max_length=400)
    image_370_by_410    =       models.ImageField(blank=True, null=True)
    image_570_by_640    =       models.ImageField(blank=True, null=True)
    slug                    =       models.SlugField(max_length=200, blank=True, null=True)
    designation         =       models.CharField(max_length=200)
    speech                    =       models.TextField(blank=True, null=True)
    image_770_by_445    =       models.ImageField(blank=True, null=True)
    status              =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)

    class Meta:
    	verbose_name = 'Team'
    	verbose_name_plural = 'Team'

    def __str__(self):
    	return self.full_name

    def get_absolute_url(self):
        return reverse("team:team_details", args=[self.id, self.slug])


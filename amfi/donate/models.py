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




class Donate(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    TRAINING = (
        ('Computer Training (Desktop Publishing)','Computer Training (Desktop Publishing)'),
        ('Musical Instruments (Piano/ Guitar)','Musical Instruments (Piano/ Guitar)'),
        ('Photography And Video Editing','Photography And Video Editing'),
        ('Communication Management','Communication Management'),
        ('Web Designing And Hosting','Web Designing And Hosting'),
        ('Insurance Administration','Insurance Administration'),
        ('Catering And Small Chops','Catering And Small Chops'),
        ('Project Management','Project Management'),
        ('Fashion Designing','Fashion Designing'),
        ('Gele Tying','Gele Tying'),
        ('Hair Making','Hair Making'),
        ('Communication Management','Communication Management'),
        ('Make Over','Make Over'),
        ('Craft','Craft'),
        ('Sound Engineering','Sound Engineering'),
        ('Acting/Dancing','Acting/Dancing'),
        ('CV Clinic','CV Clinic'),
    )
    status              =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    title          =       models.CharField(max_length=1000, choices=BLANK_CHOICE_DASH + list(TRAINING))
    fees          		=      	models.TextField(blank=True, null=True)
    image_670_by_478    =       models.ImageField(blank=True, null=True)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)

    class Meta:
    	verbose_name = 'Donation'
    	verbose_name_plural = 'Donations'

    def __str__(self):
    	return self.full_name


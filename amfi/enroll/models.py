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





class Enroll(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    PARISH = (
    	('St. John the Evangelist Agah','St. John the Evangelist Agah'),
        ('St. Jude Thadius Erunwe','St. Jude Thadius Erunwe'),
        ('St. Anthony Mary Claret Eyita','St. Anthony Mary Claret Eyita'),
        ('St. Augustine Ikorodu','St. Augustine Ikorodu'),
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
    full_name               =       models.CharField(max_length=200, blank=True, null=True)
    email               =       models.EmailField(blank=True, null=True)
    phone_number        =       models.CharField(max_length=200, blank=True, null=True)
    address         =       models.TextField(blank=True, null=True)
    training              =       models.CharField(max_length=1000, choices=BLANK_CHOICE_DASH + list(TRAINING))
    your_parish              =       models.CharField(max_length=1000, choices=BLANK_CHOICE_DASH + list(PARISH))
    
    view_count          =       models.PositiveIntegerField(default=0)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-id']
        verbose_name = 'Enroll'
        verbose_name_plural = 'Enroll'

    def __str__(self):
        return self.full_name





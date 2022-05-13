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
# Create your models here.



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")





class Home(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    status              =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    title               =       models.CharField(max_length=200)
    slug                =       models.SlugField(max_length=200)
    author              =       models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    description         =       models.TextField()
    video               =       models.FileField(blank=True, null=True)
    image               =       models.ImageField(blank=True, null=True)
    view_count          =       models.PositiveIntegerField(default=0)
    created             =       models.DateTimeField(auto_now_add=True)
    updated             =       models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-id']
        verbose_name = 'Home'
        verbose_name_plural = 'Home'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("home:home_detail", args=[self.id, self.slug])


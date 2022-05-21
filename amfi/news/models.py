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





class News(models.Model):
    objects = models.Manager()      #Our default Manager
    published = PublishedManager()  #Our Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    status                  =       models.CharField(max_length=10, choices=BLANK_CHOICE_DASH + list(STATUS_CHOICES))
    author               	=       models.CharField(max_length=200, blank=True, null=True)
    title                   =       models.CharField(max_length=1000, blank=True, null=True)
    slug                	=       models.SlugField(max_length=200, blank=True, null=True)
    image_770_by_450    	=       models.ImageField(blank=True, null=True)
    video_link              =       models.CharField(max_length=1000, blank=True, null=True)
    body                	=       models.TextField(blank=True, null=True)
    quote                	=       models.TextField(blank=True, null=True)
    body_2               	=       models.TextField(blank=True, null=True)
    view_count          	=       models.PositiveIntegerField(default=0)
    created             	=       models.DateTimeField(auto_now_add=True)
    updated             	=       models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-id']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("news:news_details", args=[self.id, self.slug])


@receiver(pre_save, sender=News)
def pre_save_slug1(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug




class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    full_name 					=	models.CharField(max_length=150, blank=True)
    email 						=	models.EmailField(blank=False, null=False)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name="replies")
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return 'News Title: \n{} \n \nComment by: {} {}\n'.format(self.post.title, str(self.first_name), str(self.last_name))
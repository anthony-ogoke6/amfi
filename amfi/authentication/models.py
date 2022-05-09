from __future__ import unicode_literals

from django.db import models

from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):
    """ User Manager that knows how to create users via email instead of username """
    def create_user(self, email, password=None):
        email = self.normalize_email(email)
        if email is None:
            raise TypeError('User should have an Email')
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
	objects 					=	UserManager()
	REQUIRED_FIELDS 			=	[]
	USERNAME_FIELD 				=	"email"
	username 					=	None
	email 						=	models.EmailField(blank=False, null=False, unique=True)
	first_name 					=	models.CharField(max_length=150, blank=True)
	last_name 					=	models.CharField(max_length=150, blank=True)
	is_verified                 =   models.BooleanField(default=False)
	is_staff                 =   models.BooleanField(default=False)
	is_active                   =   models.BooleanField(default=True)
	phone_number    			=	models.CharField(max_length=200, blank=True, null=True)
	created_at                  =   models.DateTimeField(auto_now_add=True)
	updated                     =   models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.email

	# def tokens(self):
	# 	refresh = RefreshToken.for_user(self)
	# 	return {
	#     	'refresh': str(refresh),
	#     	'access': str(refresh.access_token)
	#     }





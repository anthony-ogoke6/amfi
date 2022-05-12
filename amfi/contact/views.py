from django.contrib.humanize.templatetags.humanize import naturaltime, intcomma
import requests
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.views import View
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Count
import hmac
import hashlib
import json
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *


import logging

logger = logging.getLogger(__name__)



def contact(request):
	if request.method == 'POST':
		#contact_form = ContactForm(request.POST or None)
		#if contact_form.is_valid():
		full_name = request.POST['full_name']
		email = request.POST['email']
		phone_number = request.POST['phone_number']
		topic = request.POST['subject']
		message = request.POST['message']
		contact_form = ContactMessage(full_name=full_name, email=email, phone_number=phone_number, subject=topic, message=message)
		contact_form.save()
		subject = f"{full_name} Sent a contact message from AMFI Website"
		msg = f"Full Name: {full_name}\n \nEmail: {email}\n \nPhone Number: {phone_number}\n \nSubject: {topic}\n \nMessage: {message}"
		message = '%s ' %(msg)
		emailFrom = settings.EMAIL_HOST_USER
		emailTo = [settings.EMAIL_HOST_USER, email]
		send_mail(subject, message, emailFrom, emailTo )
		messages.success(request, "Message sent successfully, we will reach out to you shortly", extra_tags='success')
		return redirect('contact:contact')
		#else:
		# messages.success(request, "Message not sent.", extra_tags='error')
		# return redirect('contact:contact')

	else:
		contact = Contact.objects.all()
	context = {
        'contact': contact,
        }
	return render(request, 'contact/contact.html', context)


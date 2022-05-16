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
from contact.models import *
from training.models import *


import logging

logger = logging.getLogger(__name__)


# Create your views here.

def enroll(request):
	if request.method == 'POST':
		#contact_form = ContactForm(request.POST or None)
		#if contact_form.is_valid():
		full_name = request.POST['full_name']
		email = request.POST['email']
		phone_number = request.POST['phone_number']
		address = request.POST['address']
		training = request.POST['training']
		your_parish = request.POST['your_parish']
		try:
			enter_your_parish = request.POST['enter_your_parish']
		except:
			enter_your_parish = ''
		# training_info = Training.objects.get(title=training)
		# try:
		# 	amount = training_info.amount
		# except:
		amount = str(2000) + "00"
		#amount = int(str(course.amount) + "00")
		enroll = Enroll(
			form_amount=2000,
			full_name=full_name, 
			email=email, 
			phone_number=phone_number, 
			address=address, 
			training=training,
			your_parish=your_parish,
			enter_your_parish=enter_your_parish)
		enroll.save()
		reference = str(enroll.reference)
		payment_status = enroll.payment_status
		subject = f"{full_name} wants to enroll for {training} from AMFI Website"
		msg = f"Full Name: {full_name}\n \nPayment Status: {payment_status}\n \nReference: {reference}\n \nEmail: {email}\n \nPhone Number: {phone_number}\n \nAddress: {address}\n \nTraning: {training}\n \nParish/Outsation: {your_parish}"
		message = '%s ' %(msg)
		emailFrom = settings.EMAIL_HOST_USER
		emailTo = [settings.EMAIL_HOST_USER]
		try:
			send_mail(subject, message, emailFrom, emailTo )
		except:
			pass
		data = {
				"email": email,
				"amount": amount,
				"reference": reference,
				"metadata": {
			         "custom_fields": [
			            {
			                "display_name": full_name,
			                "variable_name": training,
			                "value": phone_number
			            }
			        ]
			    }
			}
		#data = {"reference": reference, "amount": amount, "email": email}
		url = "https://api.paystack.co/transaction/initialize"
		
		headers = {
	        'Authorization': 'Bearer sk_live_ffb5db8bf8d3abe7f343a743ae58ac5911c68d11',
	        'Content-Type': 'application/json',
	        }
		response = requests.request("POST", url, headers=headers, json=data)
		res = response.json()
		try:
			checkout = res['data']['authorization_url']
		except:
			messages.success(request, "Payment processing error. Kindly visit AMFI office to purchase the form", extra_tags='error')
			return redirect('enroll:enroll')
		return redirect(checkout)
		
		#else:
		# messages.success(request, "Message not sent.", extra_tags='error')
		# return redirect('contact:contact')

	else:
		enroll = EnrollForm()
		contact = Contact.objects.all()
	context = {
        'enroll': enroll,
        'contact': contact,
        }
	return render(request, 'enroll/enroll.html', context)



def thank_you(request):
	training = Training.objects.all()
	context = {
        'training': training,
	}
	messages.success(request, "Thanks, a mail will be sent to you once form payment is verified.", extra_tags='success')
	return render(request, 'training/events.html', context)



@csrf_exempt
def processPaystackWebhook(request):
    if request.method == 'POST':
        json_body = json.loads(request.body)
        #paystack_sk = "sk_live_ffb5db8bf8d3abe7f343a743ae58ac5911c68d11"
        #paystack_sk = "sk_test_3be5de37862bdd6a684d0f2fe08c2ef6dfbb5111"
        x_forwarded_for = request.META.get('HTTP_X_FORWADED_FOR')
        if x_forwarded_for:
        	ip = x_forwarded_for.split(',')[0]
        else:
        	ip = request.META.get('REMOTE_ADDR')
        paystac_ip = ["52.31.139.75", "52.49.173.169", "52.214.14.220", "10.0.0.124"]
        if str(ip) in paystac_ip:
            status = json_body['data']['status']
            if status == "success":
                reference = json_body['data']['reference']
                if reference:
        	        try:
        	            user_reference = Enroll.objects.get(reference=reference)
        	            if user_reference:
        	                    training = user_reference.training
        	                    full_name = user_reference.full_name
        	                    user_reference.payment_status = True
        	                    user_reference.save()
        	                    subject = f"Webhook from paystack via AMFI"
        	                    message = '%s ' %(f"\nHello {full_name}\n \nYour {user_reference.amount} NGN form payment for the AMFI {training} training has been successfuly verified. You have been added to the {training} training class.\n \nVisit the AMFI admin office at St. Augustines Catholic Church Ikorodu if you have further enquiries",)
        	                    emailFrom = settings.EMAIL_HOST_USER
        	                    emailTo = [settings.EMAIL_HOST_USER, user_reference.email]
        	                    send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
        	                    return HttpResponse(status=200)
                	except ObjectDoesNotExist:
                		return HttpResponse(status=400)

    return HttpResponse(status=400)


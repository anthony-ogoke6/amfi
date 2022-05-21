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


def news(request):
	news = News.published.all()
	query = request.GET.get('q')
	if query:
		news = News.published.filter(
			Q(title__icontains=query)|
			Q(author__icontains=query)|
			Q(body__icontains=query)|
			Q(body_2__icontains=query)|
			Q(quote__icontains=query)
		).distinct()
	else:
		pass
	context = {'news': news}
	return render(request, 'news/news-standard.html', context)


def news_details(request, id, slug):
	news_increament = get_object_or_404(News, id=id, slug=slug)
	news_increament.view_count +=1
	news_increament.save()
	related = []
	news = get_object_or_404(News, id=id, slug=slug)
	q = news.title
	search = request.GET.get('search')
	if search:
		news = News.published.filter(
			Q(title__icontains=search)|
			Q(author__icontains=search)|
			Q(body__icontains=search)|
			Q(body_2__icontains=search)|
			Q(quote__icontains=search)
			)
	else:
		pass
	similar = News.published.filter(
		Q(title__icontains=q)
	)

	if len(similar)==2:
		related.append(similar[1])
	elif len(similar)==3:
		related.append(similar[1])
		related.append(similar[2])
	elif len(similar)>3:
		related.append(similar[1])
		related.append(similar[2])
		related.append(similar[3])
	else:
		pass

	if request.method == 'POST':
		comment_form = CommentForm(request.POST or None)
		if comment_form.is_valid():
			content = request.POST.get('content')
			reply_id = request.POST.get('comment_id')
			comment_qs = None
			if reply_id:
				comment_qs = Comment.objects.get(id=reply_id)
			comment = Comment.objects.create(post=news, first_name=request.full_name, content=content, reply=comment_qs)
			comment.save()
		comments1 = Comment.objects.filter(post=news, reply=None).order_by('-id')
		email_list = []
		if comments1:
			for comment in comments1:
				try:
					email = comment.email
				except:
					email = settings.EMAIL_HOST_USER

				if email in email_list:
					pass
				else:
					email_list.append(email)
		if email in email_list:
			pass
		else:
			email_list.append(settings.EMAIL_HOST_USER)

		if comment_form.is_valid():
			content = request.POST.get('content')
			reply_id = request.POST.get('comment_id')
			email_msg = []
			for email in email_list:
				if str(email) == str(request.email):
					pass
				else:
					email_msg.append(email)
			if reply_id:
				reply_email = []
				comment_qs = Comment.objects.get(id=reply_id)
				email_owner_comment = comment_qs.email
				for reply in comment_qs.replies.all():
					user_email = reply.email
					if user_email in reply_email:
						pass
					else:
						reply_email.append(user_email)
					if email_owner_comment in reply_email:
						pass
					else:
						reply_email.append(email_owner_comment)
						print(reply_email)

				reply_email_list = []
				for mail in reply_email:
					if str(mail) == str(request.email):
						pass
					else:
						reply_email_list.append(mail)

				reply_email_list.append(settings.EMAIL_HOST_USER)
				subject = 'Comments reply from AMFI Website'
				message = '%s %s' %(comment_qs, f"\nreply by: {request.full_name} \n \nContent: \n{content} \n \n \nhttps://www.amfiinstitute.com{news.get_absolute_url()}",)
				print(reply_email_list)
				emailFrom = settings.EMAIL_HOST_USER
				emailTo = reply_email_list
				send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
			else:
				messge_content = f"News Title: \n{news.title} \n \nComment by: {request.full_name} \n \nContent: \n{content} \n \n \nhttps://www.amfiinstitute.com{news.get_absolute_url()}"
				subject = "New comment from AMFI Website"
				message = '%s' %(messge_content)
				emailFrom = settings.EMAIL_HOST_USER
				emailTo = email_msg
				send_mail(subject, message, emailFrom, emailTo, fail_silently=True )
	else:
		comment_form= CommentForm()

	context = {
	'news': news,
	'related': related,
	}

	return render(request, 'news/news-details.html', context)




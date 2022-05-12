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
from .models import Project


import logging

logger = logging.getLogger(__name__)


# Create your views here.


def projects(request):
	projects = Project.objects.all()
	context = {
        'projects': projects,
        }
	return render(request, 'projects/project-2.html', context)


def project_details(request, id, slug):
	project_increament = get_object_or_404(Project, id=id, slug=slug)
	project_increament.view_count +=1
	project_increament.save()
	project = get_object_or_404(Project, id=id, slug=slug)
	context = {
		'project': project,
	}
	return render(request, 'projects/project-details.html', context)



# def project_details(request, id, slug):
#     return render(request, 'projects/project-details.html')


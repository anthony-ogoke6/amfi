"""amfi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from enroll import views as enroll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace="home")),
    path('about/', include('about.urls', namespace="about")),
    path('auth/', include('authentication.urls', namespace="auth")),
    path('contact/', include('contact.urls', namespace="contact")),
    path('training/', include('training.urls', namespace="training")),
    path('projects/', include('projects.urls', namespace="projects")),
    path('enroll/', include('enroll.urls', namespace="enroll")),
    path('news/', include('news.urls', namespace="news")),
    path('testimonial/', include('testimonial.urls', namespace="testimonial")),
    path('team/', include('team.urls', namespace="team")),
    path('faq/', include('faq.urls', namespace="faq")),
    path('board/', include('board.urls', namespace="board")),
    path('paystack_confirmation/', enroll_views.processPaystackWebhook, name="paystack_confirmation"),
    path('thank_you/', enroll_views.thank_you, name="thank_you"),
    path('summernote/', include('django_summernote.urls')),
]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


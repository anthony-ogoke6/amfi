from django.urls import path, re_path


from . import views

app_name = 'news'
urlpatterns = [
    path('', views.news, name='news'),
    re_path(r'news_details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.news_details, name="news_details"),
]
from django.urls import path, re_path


from . import views

app_name = 'team'
urlpatterns = [
    path('', views.team, name='team'),
    re_path(r'team_details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.team_details, name="team_details"),
]
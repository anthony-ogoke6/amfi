from django.urls import path, re_path


from . import views

app_name = 'projects'
urlpatterns = [
    path('', views.projects, name='projects'),
    path('', views.project_details, name='projects'),
    re_path(r'project_details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.project_details, name="project_details"),
]
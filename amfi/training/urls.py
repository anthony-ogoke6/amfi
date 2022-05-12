from django.urls import path, re_path


from . import views

app_name = 'training'

urlpatterns = [
    path('', views.training, name='training'),
    re_path(r'training_details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.training_details, name="training_details"),
]
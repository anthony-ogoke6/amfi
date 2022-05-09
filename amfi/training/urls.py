from django.urls import path, re_path


from . import views

app_name = 'training'
urlpatterns = [
    path('', views.training, name='training'),
]
from django.urls import path, re_path


from . import views

app_name = 'emergency'
urlpatterns = [
    path('', views.emergency, name='emergency'),
]
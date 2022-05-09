from django.urls import path, re_path


from . import views

app_name = 'about'
urlpatterns = [
    path('', views.about, name='about'),
]
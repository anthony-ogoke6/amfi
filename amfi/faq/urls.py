from django.urls import path, re_path


from . import views

app_name = 'faq'
urlpatterns = [
    path('', views.faq, name='faq')
]
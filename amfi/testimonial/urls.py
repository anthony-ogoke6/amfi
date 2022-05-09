from django.urls import path, re_path


from . import views

app_name = 'testimonial'
urlpatterns = [
    path('', views.testimonials, name='testimonial'),
    
]
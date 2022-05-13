from django.urls import path, re_path


from . import views

app_name = 'board'
urlpatterns = [
    path('', views.board, name='board'),
    re_path(r'board_details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.board_details, name="board_details"),
]
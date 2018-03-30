from django.urls import path, re_path
from . import views

urlpatterns= [
     re_path(r'^$',views.index, name='index'),
     re_path(r'^details/(?P<id>\d+)/$',views.details, name='details') 
    #  The new path() syntax in Django 2.0 does not use regular expressions. You want something like:
    #  path('<int:album_id>/', views.detail, name='detail'),
    #  If you want to use a regular expression, you can use re_path().
    #  re_path(r'^(?P<album_id>[0-9])/$', views.detail, name='detail')
] 
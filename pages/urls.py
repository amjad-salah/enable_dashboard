from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('articles/', views.articles, name='articles'),
    path('announcements/', views.announcements, name='announcements'),
]

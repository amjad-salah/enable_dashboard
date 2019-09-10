from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcements, name='announcements'),
    path('<int:id>', views.announcement, name='announcement'),
]
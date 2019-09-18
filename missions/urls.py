from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='missions'),
    path('<int:id>', views.mission, name='mission'),
]
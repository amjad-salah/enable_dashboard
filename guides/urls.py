from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='guides'),
    path('<int:id>', views.guide, name='guide'),
]
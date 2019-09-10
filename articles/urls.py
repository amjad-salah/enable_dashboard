from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='articles'),
    path('<int:id>', views.article, name='article'),
]
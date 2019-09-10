from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'pages/index.html')


def meetings(request):
  return render(request, 'pages/meetings.html')


def articles(request):
  return render(request, 'pages/articles.html')


def announcements(request):
  return render(request, 'pages/announcements.html')

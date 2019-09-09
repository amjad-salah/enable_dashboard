from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'pages/index.html')


def meetings(request):
    return render(request, 'pages/meetings.html')

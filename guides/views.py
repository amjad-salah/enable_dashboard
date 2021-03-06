from django.shortcuts import render
from .models import Guide

def index(request):
  guides = Guide.objects.all()
  context = {
    'guides': guides
  }
  return render(request, 'guides/guides.html', context)

def guide(request, id):
  guide = Guide.objects.get(id=id)
  context = {
    'guide': guide
  }
  return render(request, 'guides/guide.html', context)

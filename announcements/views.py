from django.shortcuts import render
from .models import Announcement

def announcements(request):
  announcements = Announcement.objects.all().order_by('-created_date')
  context = {
    'announcements': announcements
  }
  return render(request, 'announcements/announcements.html', context)

def announcement(request, id):
  announcement = Announcement.objects.get(id=id)
  context = {
    'announcement': announcement
  }
  return render(request, 'announcements/announcement.html', context)

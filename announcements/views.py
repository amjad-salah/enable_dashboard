from django.shortcuts import render

def announcements(request):
  return render(request, 'announcements/announcements.html')

def announcement(request):
  return render(request, 'announcements/announcement.html')

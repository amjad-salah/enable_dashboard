from django.shortcuts import render

def announcements(request):
  return render(request, 'announcements/announcements.html')

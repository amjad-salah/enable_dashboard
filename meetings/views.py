from django.shortcuts import render
from .models import Meeting

def meetings(request):
  meetings = Meeting.objects.filter(finished=False).order_by('-date')
  context = {
    'meetings': meetings
  }
  return render(request, 'meetings/meetings.html', context)

def meeting(request, id):
  meeting = Meeting.objects.get(id=id)
  context = {
    'meeting': meeting
  }
  return render(request, 'meetings/meeting.html', context)

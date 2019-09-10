from django.shortcuts import render

def meetings(request):
  return render(request, 'meetings/meetings.html')

def meeting(request):
  return render(request, 'meetings/meeting.html')

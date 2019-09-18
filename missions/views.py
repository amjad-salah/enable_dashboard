from django.shortcuts import render

def index(request):
  return render(request, 'missions/missions.html')

def mission(request, id):
  return render(request, 'missions/mission.html')

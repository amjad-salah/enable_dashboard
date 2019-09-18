from django.shortcuts import render
from .models import Mission

def index(request):
  missions = Mission.objects.all().order_by('from_date')
  context = {
    'missions': missions
  }
  return render(request, 'missions/missions.html', context)

def mission(request, id):
  mission = Mission.objects.get(id=id)
  context = {
    'mission': mission
  }
  return render(request, 'missions/mission.html', context)

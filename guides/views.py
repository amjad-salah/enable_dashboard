from django.shortcuts import render

def index(request):
  return render(request, 'guides/guides.html')

def guide(request, id):
  return render(request, 'guides/guide.html')

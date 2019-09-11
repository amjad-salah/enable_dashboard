from django.shortcuts import render
from django.http import HttpResponse

from announcements.models import Announcement
from meetings.models import Meeting
from articles.models import Article


def index(request):
  announcements = Announcement.objects.order_by('-created_date')[:3]
  meetings = Meeting.objects.order_by('-date').filter(finished=False)[:3]
  articles = Article.objects.order_by('-created_date').filter(publish=True)[:3]

  context = {
    'announcements': announcements,
    'meetings': meetings,
    'articles': articles
  }
  return render(request, 'pages/index.html', context)




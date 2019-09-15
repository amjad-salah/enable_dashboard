from django.shortcuts import render
from django.http import HttpResponse

from announcements.models import Announcement
from meetings.models import Meeting
from articles.models import Article


def index(request):
  articles = Article.objects.order_by('-created_date').filter(publish=True)[:3]

  context = {
    'articles': articles
  }
  return render(request, 'pages/index.html', context)




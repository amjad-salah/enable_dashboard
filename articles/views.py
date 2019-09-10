from django.shortcuts import render
from .models import Article

def index(request):
  articles = Article.objects.all().order_by('-created_date')
  context = {
    'articles': articles
  }
  return render(request, 'articles/articles.html', context)

def article(request, id):
  return render(request, 'articles/article.html')

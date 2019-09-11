from django.shortcuts import render
from .models import Article

def index(request):
  articles = Article.objects.filter(publish=True).order_by('-created_date')
  context = {
    'articles': articles
  }
  return render(request, 'articles/articles.html', context)

def article(request, id):
  article = Article.objects.get(id=id)
  context = {
    'article': article
  }
  return render(request, 'articles/article.html', context)

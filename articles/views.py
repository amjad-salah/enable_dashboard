from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article

def index(request):
  articles = Article.objects.filter(publish=True).order_by('-created_date')
  paginator = Paginator(articles, 15)
  page = request.GET.get('page')
  paged_articles = paginator.get_page(page)
  context = {
    'articles': paged_articles
  }
  return render(request, 'articles/articles.html', context)

def article(request, id):
  article = Article.objects.get(id=id)
  context = {
    'article': article
  }
  return render(request, 'articles/article.html', context)

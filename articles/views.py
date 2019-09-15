from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Article, Comment

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
  comments = Comment.objects.filter(articl=id)
  context = {
    'article': article,
    'comments': comments
  }
  if request.method == 'POST':
    user = request.user
    articl = Article.objects.get(id=id)
    body = request.POST['body']
    comment = Comment(user=user, articl=articl, body=body)
    comment.save()
    return render(request, 'articles/article.html', context)
  else:
    return render(request, 'articles/article.html', context)

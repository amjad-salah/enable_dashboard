from django.shortcuts import render

def articles(request):
  return render(request, 'articles/articles.html')

def article(request):
  return render(request, 'articles/article.html')

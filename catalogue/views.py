from django.shortcuts import render
from django.http import Http404
from .models import Article

def home_page(request):
    return render(request, 'home_page.html')

def list_article(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def article(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'article.html', {'article': article})
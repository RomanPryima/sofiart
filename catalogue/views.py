from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home_page(request):
    articles = Article.objects.all()
    articles_names = list()

    for article in articles:
        articles_names.append(article.name)

    response_html = '<br>'.join(articles_names)

    return render(request, 'home_page.html', {'articles': articles})
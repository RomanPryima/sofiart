from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import NewArticleForm
from .models import Article

def home_page(request):
    return render(request, 'home_page.html')

def list_article(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'article': article})

def new_article(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.published = timezone.now()
            import pdb
            pdb.set_trace()
            article.image = request.FILES['image']
            article.save()
            return redirect('article', slug=article.slug)
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {'form': form})

def new_article(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.published = timezone.now()
            article.image = request.FILES.get('image')
            article.save()
            return redirect('article', slug=article.slug)
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {'form': form})

def edit_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = NewArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.published = timezone.now()
            article.image = request.FILES.get('image')
            article.save()
            return redirect('article', slug=article.slug)
    else:
        form = NewArticleForm(instance=article)
    return render(request, 'new_article.html', {'form': form, 'article':article})
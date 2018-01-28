from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import NewArticleForm
from .models import Article, GalleryImage

def home_page(request):
    return render(request, 'home_page.html')

def list_article(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'article.html', {'article': article})

def edit_article(request, slug=None):
    article = None
    gallery_form = None
    if slug:
        article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        if 'delete-article' in request.POST:
            article.delete()
            return redirect('list_article')
        form = NewArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.creator = request.user
            article.published = timezone.now()
            if request.FILES.get('image'):
                article.image = request.FILES.get('image')
            article.save()
            if request.FILES.get('gallery_image'):
                images = request.FILES.getlist('gallery_image')
                for image in images:
                    gallery_image = GalleryImage()
                    gallery_image.save(article=article, image=image)
            return redirect('article', slug=article.slug)
    else:
        form = NewArticleForm(instance=article)
        gallery_form = GalleryImage(article=article)
    return render(request, 'new_article.html', {'form': form, 'gallery_form': gallery_form, 'article': article})
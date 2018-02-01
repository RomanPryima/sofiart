from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import NewArticleForm
from .models import Article, GalleryImage


class ListArticleView(ListView):
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all()


class ArticleView(DetailView):
    model = Article

def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, pk=kwargs.get('object').pk)
        return context


class NewArticleView(CreateView):
    model = Article
    form_class = NewArticleForm

    def form_valid(self, *args, **kwargs):
        post_data = self.request.POST
        post_files = self.request.FILES
        article = Article(name=post_data.get('name'),
                          description=post_data.get('description'),
                          text=post_data.get('text'),
                          price=post_data.get('price'),
                          image=post_files.get('image'),
                          creator=self.request.user,
                          )
        article.save()
        if 'gallery_images' in post_files:
            for gallery_image in post_files.getlist('gallery_images'):
                image = GalleryImage()
                image.save(article=article, image=gallery_image)
        return redirect('article', pk=article.pk)

class EditArticleView(UpdateView):
    model = Article
    form_class = NewArticleForm

    def form_valid(self, *args, **kwargs):
        post_data = self.request.POST
        post_files = self.request.FILES
        article = Article.objects.get(pk=self.kwargs.get('pk'))
        article.name=post_data.get('name')
        article.description=post_data.get('description')
        article.text=post_data.get('text')
        article.price=post_data.get('price')
        if post_files.get('image'):
            article.image=post_files.get('image')
        article.creator=self.request.user
        if 'gallery_image' in post_files:
            for gallery_image in post_files.getlist('gallery_images'):
                image = GalleryImage()
                image.save(article=article, image=gallery_image)
        return redirect('article', pk=article.pk)

class DeleteArticleView(DeleteView):
    model = Article
    success_url = reverse_lazy('list_article')









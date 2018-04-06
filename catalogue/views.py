from django.db.models.query import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from .forms import *
from .models import *


class ListArticleView(ListView):
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            result = Article.objects.all().filter(Q(name__contains=query) |
                                                  Q(description__contains=query) |
                                                  Q(text__contains=query)).order_by('-created')
        else:
            result = Article.objects.all()
        return result


class ArticleView(UpdateView):
    model = Article
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        return article.get_context(context=context)

    def post(self, *args, **kwargs):
        Review().save(self.request.POST)
        return redirect('article', pk=str(self.request.POST.get('article')[0]))

    def form_valid(self):
        return bool(self.request.POST.get('Message') and self.request.POST.get('article'))


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
                          creator=self.request.user,
                          )
        article.save()
        if 'gallery_images' in post_files:
            for gallery_image in post_files.getlist('gallery_images'):
                image = GalleryImage()
                image.save(article=article, image=gallery_image, name=gallery_image.name)
        else:
            GalleryImage(article=article, image='')
        return redirect('edit_article', pk=article.pk)


class EditArticleView(UpdateView):
    model = Article
    form_class = NewArticleForm

    def form_valid(self, *args, **kwargs):
        pk = Article.update(self)
        return redirect('article', pk=pk)


class DeleteArticleView(DeleteView):
    model = Article
    success_url = reverse_lazy('list_article')

from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView, FormView
from .forms import NewArticleForm
from .models import Article, GalleryImage


class ListArticleView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(ListArticleView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.all()
        return context

class ArticleView(DetailView):

    model = Article

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article, slug=kwargs.get('object').slug)
        return context


class NewArticle(FormView):
    form_class = NewArticleForm
    template_name = 'new_article.html'
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
        try:
            article.save()
        except:
            return redirect('new_article')
        if 'gallery_image' in post_files:
            for gallery_image in post_files.getlist('gallery_image'):
                image = GalleryImage()
                image.save(article=article, image=gallery_image)
        return redirect('article', slug=article.slug)


from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^list_article/$', ListArticleView.as_view(template_name='list_article.html'), name='list_article'),
        url(r'^article/(?P<slug>[-\w]+)/$',  ArticleView.as_view(template_name='article.html'), name='article'),
        url(r'^edit_article/(?P<slug>[-\w]+)/$', NewArticle.as_view(template_name='new_article.html'), name='edit_article'),
        url(r'^new_article/$', NewArticle.as_view(template_name='new_article.html'), name='new_article'),


]
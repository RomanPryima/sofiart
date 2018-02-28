from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^$', ListArticleView.as_view(template_name='list_article.html'), name='list_article'),
        url(r'^article/add/$', staff_member_required(NewArticleView.as_view(template_name='new_article.html')), name='new_article'),
        url(r'^article/edit/(?P<pk>[-\w]+)$', staff_member_required(EditArticleView.as_view(template_name='new_article.html')), name='edit_article'),
        url(r'^article/(?P<pk>[-\w]+)/$',  ArticleView.as_view(template_name='article.html'), name='article'),
        url(r'^add_review/$',  ArticleView.as_view(template_name='article.html'), name='add_review'),
        url(r'^article/(?P<pk>[-\w]+)/delete/$', staff_member_required(DeleteArticleView.as_view()), name='delete_article'),
]

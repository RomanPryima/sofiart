from django.conf.urls import url

from .views import *

urlpatterns = [
        url(r'^list_article/$', list_article, name='list_article'),
        url(r'^new_article/$', new_article, name='new_article'),
        url(r'^article/(?P<slug>[-\w]+)/$', article, name='article'),

]
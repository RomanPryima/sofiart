from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from .views import *
from .models import Article

class HomeTests(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home_page)

    def test_home_view_contains_link_to_articles_page(self):
        self.assertContains(self.response, 'list_article')

class ListArticleTests(TestCase):
    def setUp(self):
        self.article = Article.objects.create(name=u'Прибамбас')
        url = reverse('list_article')
        self.response = self.client.get(url)

    def test_article_view_success_status_code(self):
        url = reverse('list_article')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_url_resolves_article_view(self):
        view = resolve('/list_article/')
        self.assertEquals(view.func, list_article)

    def test_home_view_contains_link_to_articles_page(self):
        article_url = reverse('article', kwargs={'slug': self.article.slug})
        self.assertContains(self.response, 'href="{}"'.format(article_url))


class ArticleTests(TestCase):
    def setUp(self):
        self.article =Article.objects.create(name=u'Прибамбас')

    def test_article_view_success_status_code(self):
        url = reverse('article', kwargs={'slug': self.article.slug})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_view_not_found_status_code(self):
        url = reverse('article', kwargs={'slug': 'aasdadfsdfh'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_article_url_resolves_article_view(self):
        view = resolve('/article/{}/'.format(self.article.slug))
        self.assertEquals(view.func, article)
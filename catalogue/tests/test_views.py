from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from catalogue.views import *
from catalogue.models import Article
from catalogue.forms import NewArticleForm

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

class NewArticleTests(TestCase):
    def setUp(self):
        self.article =Article.objects.create(name=u'Прибамбас')

    def test_new_topic_view_success_status_code(self):
        response = self.client.get('/new_article/')
        self.assertEquals(response.status_code, 200)


    def test_new_article_url_resolves_new_topic_view(self):
        view = resolve('/new_article/')
        self.assertEquals(view.func, edit_article)

    def test_edit_article_contains_form(self):
        url = reverse('edit_article', kwargs={'slug': self.article.slug})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewArticleForm)

    def test_new_article_contains_form(self):
        response = self.client.get('/new_article/')
        form = response.context.get('form')
        self.assertIsInstance(form, NewArticleForm)

    def test_edit_article_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('edit_article', kwargs={'slug': self.article.slug})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
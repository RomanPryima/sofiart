from django.contrib.auth.models import User
from django.urls import resolve
from django.test import TestCase, Client
from django.views.generic import TemplateView
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
        self.assertEquals(view.func.__name__, TemplateView.__name__)

    def test_home_view_contains_link_to_articles_page(self):
        self.assertContains(self.response, '/list_article/')

class ListArticleTests(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username="testbot", password="testbot",
            email="test@test.com"
        )
        user.save()
        client = Client()
        client.login(username="testbot", password="testbot")
        self.article = Article.objects.create(name=u'Прибамбас')
        url = reverse('list_article')
        self.response = self.client.get(url)

    def test_article_view_success_status_code(self):
        url = reverse('list_article')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_url_resolves_article_view(self):
        view = resolve('/list_article/')
        self.assertEquals(view.func.__name__, ListArticleView.__name__)

    def test_list_view_contains_link_to_article_page(self):
        article_url = reverse('article', kwargs={'pk': self.article.pk})
        self.assertContains(self.response, 'href="{}"'.format(article_url))


class ArticleTests(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(
            username="testbot", password="testbot",
            email="test@test.com"
        )
        user.save()
        client = Client()
        client.login(username="testbot", password="testbot")
        self.article =Article.objects.create(name=u'Прибамбас')

    def test_article_view_success_status_code(self):
        url = reverse('article', kwargs={'pk': self.article.pk})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_view_not_found_status_code(self):
        url = reverse('article', kwargs={'pk': '9999'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_article_url_resolves_article_view(self):
        view = resolve('/article/{}/'.format(self.article.pk))
        self.assertEquals(view.func.__name__, ArticleView.__name__)

class NewArticleTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="testbot", password="testbot",
            email="test@test.com", is_staff=True,
        )
        user.save()
        client = Client()
        client.login(username="testbot", password="testbot")
        self.article =Article.objects.create(name=u'Прибамбас')

    def test_new_topic_view_success_status_code(self):
        response = self.client.get('/article/add/')
        self.assertEquals(response.status_code, 200)


    def test_new_article_url_resolves_new_article_view(self):
        view = resolve('/article/new/')
        self.assertEquals(view.func.__name__, ArticleView.__name__)

    def test_edit_article_contains_form(self):
        url = reverse('edit_article', kwargs={'pk': self.article.pk})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewArticleForm)

    def test_new_article_contains_form(self):
        response = self.client.get('/article/add/')
        form = response.context.get('form')
        self.assertIsInstance(form, NewArticleForm)

    def test_edit_article_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('edit_article', kwargs={'pk': self.article.pk})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

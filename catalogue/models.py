from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from unidecode import unidecode


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, verbose_name='Назва')
    slug = models.SlugField(unique=False, blank=True, editable=False)
    description = models.CharField(max_length=200, blank=True, verbose_name='Опис')
    text = models.TextField(max_length=2500, blank=True, verbose_name='Текст')
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00, verbose_name='Ціна')
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    creator = models.ForeignKey(User, related_name='article', on_delete=models.CASCADE, default=1, verbose_name='Автор')

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def get_context(self, context):
        context['article'] = self
        context['title_image'] = GalleryImage.objects.get(article=self, is_title=True)
        context['gallery_images'] = GalleryImage.objects.filter(article=self, is_title=False)
        context['review_list'] = Review.objects.filter(article=self)
        return context

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Article, self).save(*args, **kwargs)

    def update(self):
        post_data = self.request.POST
        post_files = self.request.FILES
        article = Article.objects.get(pk=self.kwargs.get('pk'))
        article.name = post_data.get('name')
        article.description = post_data.get('description')
        article.text = post_data.get('text')
        article.price = post_data.get('price')
        article.creator = self.request.user
        article.save()
        if 'gallery_images' in post_files:
            for gallery_image in post_files.getlist('gallery_images'):
                image = GalleryImage()
                image.save(article=article, image=gallery_image, name=gallery_image.name)
        if 'g_image_to_delete' in post_data:
            for image_id in post_data.getlist('g_image_to_delete'):
                gallery_image = GalleryImage.objects.get(pk=image_id)
                gallery_image.delete()
        if 'is_title' in post_data:
            gallery_image = GalleryImage.objects.get(pk=post_data.get('is_title'))
            gallery_image.set_title()
        return article.pk

    class Meta:
        ordering = ('-updated',)


class GalleryImage(models.Model):
    name = models.CharField(blank=True, max_length=100)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='gallery_images', verbose_name='зображення')
    image = models.ImageField(upload_to='catalogue/images/gallery', blank=True, verbose_name='Зображення')
    is_title = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if kwargs:
            self.name = slugify(unidecode(kwargs.get('name')))
            self.article = kwargs.get('article')
            self.image = kwargs.get('image')
        super(GalleryImage, self).save()

    def set_title(self):
        titled_images = self.get_title_image()
        for image in titled_images:
            image.is_title = False
            image.save()
        self.is_title = True
        self.save()

    def get_title_image(self):
        return GalleryImage.objects.filter(article=self.article, is_title=True)


    class Meta:
        ordering = ('-created',)

class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    not_registered_user = models.CharField(max_length=100, verbose_name='незареєстрований користувач')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='review', verbose_name='відгук')
    creator = models.CharField(max_length=100, default="Анонім", verbose_name='автор відгуку')
    text = models.TextField(max_length=1000, blank=True, verbose_name='Текст')
    email = models.EmailField(blank=True)
    moderated = models.BooleanField(default=True)

    def save(self, query_dict=None):
        if query_dict:

            import pdb
            pdb.set_trace()
            self.text = query_dict.get('Message')
            self.email = query_dict.get('email')
            self.article = Article.objects.get(pk=query_dict.get('article'))
            username=query_dict.get('Name')
            self.creator = username if username else "Анонім"
        super(Review, self).save()

    def set_approved(self):
        self.moderated = True

    def set_banned(self):
        self.moderated = False

    class Meta:
        ordering = ('-created',)
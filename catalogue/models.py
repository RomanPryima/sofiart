from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from django.template.defaultfilters import slugify
from unidecode import unidecode


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, verbose_name='Назва')
    slug = models.SlugField(unique=False, blank=True, editable=False)
    description = models.CharField(max_length=200, blank=True, verbose_name='Опис')
    text = models.TextField(max_length=1500, blank=True, verbose_name='Текст')
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00, verbose_name='Ціна')
    updated = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    creator = models.ForeignKey(User, related_name='article', on_delete=models.CASCADE, default=1, verbose_name='Автор')

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Article, self).save(*args, **kwargs)

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
            self.name = slugify(unidecode(self.name))
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
    creator = models.ForeignKey(User, related_name='review', on_delete=models.CASCADE, default=None, verbose_name='Автор')
    text = models.TextField(max_length=1000, blank=True, verbose_name='Текст')
    email = models.EmailField(blank=True)
    moderated = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if kwargs:
            self.text = str(kwargs.get('Message')[0])
            self.email = str(kwargs.get('email')[0])
            self.article = Article.objects.get(pk=str(kwargs.get('article')[0]))
            try:
                creator = User.objects.get(username=str(kwargs.get('Name')[0]))
                self.creator = creator
            except Exception:
                pass
        super(Review, self).save()

    def set_approved(self):
        self.moderated = True

    def set_banned(self):
        self.moderated = False

    class Meta:
        ordering = ('-created',)
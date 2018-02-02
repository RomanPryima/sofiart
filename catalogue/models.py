from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
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
    image = models.ImageField(
        upload_to='catalogue/images', blank=True, verbose_name='Зображення')
    creator = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE, default=1, verbose_name='Автор')

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
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='gallery_images', verbose_name='стаття')
    image = models.ImageField(upload_to='catalogue/images/gallery', blank=True, verbose_name='Зображення')
    is_title = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.name = slugify(unidecode(self.name))
        self.article = kwargs.get('article')
        self.image = kwargs.get('image')
        super(GalleryImage, self).save()

    def set_title(self):
        titled_images = GalleryImage.objects.filter(article=self.article, is_title=True)
        for image in titled_images:
            image.is_title = False
            image.save()

        import pdb
        pdb.set_trace()
        self.is_title = True
        self.save()


    class Meta:
        ordering = ('-created',)

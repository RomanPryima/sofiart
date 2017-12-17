from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from unidecode import unidecode


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False, verbose_name='Назва')
    slug = models.SlugField(blank=True, editable=False)
    description = models.CharField(max_length=200, blank=True, verbose_name='Опис')
    text = models.TextField(max_length=1500, blank=True, verbose_name='Текст')
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00, verbose_name='Ціна')
    published = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(
        upload_to='catalogue/images', default='', blank=True, verbose_name='Зображення')
    creator = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE, default=1, verbose_name='Автор')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-published',)

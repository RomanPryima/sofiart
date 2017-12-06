from django.db import models
from django.contrib.auth.models import User



class Article(models.Model):
    number = models.CharField(max_length=5, unique=True)
    name = models.TextField(max_length=45, blank=True)
    description = models.TextField(max_length=500, blank=True)
    published = models.DateTimeField(auto_now_add=True, blank=True)
    creator = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
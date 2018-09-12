from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):

    class Meta:
        ordering = ['-posted']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'

    title = models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')
    description = models.TextField(verbose_name='Короткий опис')
    content = models.TextField(verbose_name='Повний опис')
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Дата публікації')
    is_commentable = models.BooleanField(default=True, verbose_name='Можливість коментування')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        ordering = ['-posted']
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'

    content = models.TextField(verbose_name='Кометар')
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Дата публікації')
    user = models.CharField(max_length=50, blank=True, verbose_name='Користувач')

    def __str__(self):
        return self.content[:50]


from django.db import models
from datetime import datetime

# Create your models here.

class News(models.Model):
    class Meta:
        ordering = ['-posted']
        verbose_name = 'новина'
        verbose_name_plural = 'новини'

    title = models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')
    description = models.TextField(verbose_name='Короткий опис')
    content = models.TextField(verbose_name='Повен зміст')
    posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name='Публікація')

    def __str__(self):
        return self.title
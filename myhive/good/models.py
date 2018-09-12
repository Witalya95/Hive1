from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        ordering = ['name']
        verbose_name = 'категорія'
        verbose_name_plural = 'категорії'

    name = models.CharField(max_length=30, db_index=True, unique=True, verbose_name='Назва')
    order = models.PositiveSmallIntegerField(default=0, db_index=True, verbose_name='Порядковий номер')

    def __str__(self):
        return self.name


class Good(models.Model):

    class Meta:
        ordering = ['name']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    name = models.CharField(max_length=50, verbose_name='Назва')
    description = models.TextField(verbose_name='Короткий опис')
    content = models.TextField(verbose_name='Повний опис')
    photo = models.ImageField(upload_to="goods", blank=True, verbose_name="Фото", null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Категорія')

    def __str__(self):
        return self.name
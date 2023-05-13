from enum import unique

from django.db import models
from django.urls import reverse


class Cloth(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование ткани')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    type = models.CharField(max_length=200, verbose_name='Состав ткани')
    color = models.CharField(max_length=50, verbose_name='Цвет ткани')
    quantity = models.IntegerField(verbose_name='Количество в наличии')
    description = models.TextField(verbose_name='Описание', blank=True)
    size = models.CharField(max_length=200, verbose_name='Размеры')
    price = models.IntegerField(verbose_name='Цена', blank=True)
    picture = models.ImageField(upload_to='picture/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card', kwargs={'card_id': self.pk})

    class Meta:
        verbose_name = 'Ткани'
        verbose_name_plural = 'Ткани'
        ordering = ('name', 'price')


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('title',)

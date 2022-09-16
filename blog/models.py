from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Категория: (pk={self.pk}, title={self.title})'


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='название продукта')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Изоброжение')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Статья: (pk={self.pk}, title={self.title})'


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

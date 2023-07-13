from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=100)


class News(models.Model):
    title = models.CharField(verbose_name='Название', max_length=200)
    body = RichTextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата')
    image = models.ImageField(upload_to='news', verbose_name='Изображение')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ('-date',)

    def __str__(self):
        return self.title

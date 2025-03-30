from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blog/img', blank=True, null=True, verbose_name='Изображение',)
    created_at = models.DateField(verbose_name='Дата публикации', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Признак публикации', default=True)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['title', 'created_at', 'views_count']

    def __str__(self):
        return f'{self.title}, {self.created_at}, {self.views_count}'

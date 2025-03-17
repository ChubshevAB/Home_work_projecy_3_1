from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование категории',)
    description = models.TextField(verbose_name='Описание', help_text='Введите описание категории', blank=True, null=True,)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование', help_text='Введите наименование продукта',)
    description = models.TextField(verbose_name='Описание', help_text='Введите описание продукта', blank=True, null=True,)
    image = models.ImageField(upload_to='my_app/img', blank=True, null=True, verbose_name='Фото',)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='products',)
    price = models.IntegerField(verbose_name='Цена за покупку',)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания',)
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения',)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', 'category', 'price']

    def __str__(self):
        return f'{self.name}, {self.price}'

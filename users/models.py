from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', unique=True, help_text='Введите адрес электронной почты')
    avatar = models.ImageField(verbose_name='Фото', upload_to='users/avatars/', blank=True, null=True, help_text='Загрузите фото')
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=30, blank=True, null=True, help_text='Введите номер телефона')
    country = models.CharField(verbose_name='Страна', max_length=50, help_text='Укажите страну')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

from django.db import models
from django.urls import reverse_lazy

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    taxpayer = models.PositiveIntegerField(verbose_name="ИНН", blank=True, null=True)
    middle_name = models.CharField(max_length=255, verbose_name="Отчество", blank=True, null=True)
    avatar = models.ImageField(upload_to='profile/avatar/', null=True, blank=True, default="profile/avatar/avatar.webp")
    telegram_url = models.URLField(null=True, blank=True, default="https://t.me")

    def get_absolute_url(self,):
        return reverse_lazy('user_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

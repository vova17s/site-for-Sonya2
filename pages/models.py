from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(max_length=100, verbose_name="Email")
    text = models.TextField(blank=False, verbose_name="Описание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Заявка"
        verbose_name_plural="Заявки"

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos', verbose_name='Фотография', null=True, blank=True)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
from django.db import models
from django.urls import reverse


class Goods(models.Model):
    title = models.CharField(max_length=150, verbose_name='title')
    image = models.ImageField(upload_to='invite/images', verbose_name='image')
    price = models.IntegerField(blank=True, verbose_name='price')

    def get_absolute_url(self):
        return reverse('goods', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title} -- {self.price}'


class Person(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def get_absolute_url(self):
        return reverse('person', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} {self.last_name} // [{self.pk}]'

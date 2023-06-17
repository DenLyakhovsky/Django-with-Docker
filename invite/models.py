from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=150, verbose_name='name')
    last_name = models.CharField(max_length=150, verbose_name='last_name')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def get_absolute_url(self):
        return reverse('person', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.name} {self.last_name} // [{self.pk}]'

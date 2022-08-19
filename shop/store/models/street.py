from django.db import models

from store.models import (
    Town,
)


class Street(models.Model):
    """Модель улицы"""

    name = models.CharField(
        verbose_name='Название города',
        max_length=256,
        null=False,
        blank=True,
    )

    town = models.ForeignKey(
        Town,
        verbose_name='Город',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'street'
        verbose_name = 'Улицы'
        verbose_name_plural = 'Улица'
        ordering = ['town', ]

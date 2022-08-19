from django.db import models

from store.models import (
    Town,
    Street,
)


class Shop(models.Model):
    """Модель Магазина"""

    name = models.CharField(
        verbose_name='Название магазина',
        max_length=256,
        null=False,
        blank=True,
    )

    town = models.ForeignKey(
        Town,
        verbose_name='Город',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    street = models.ForeignKey(
        Street,
        verbose_name='Улица',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    house = models.CharField(
        verbose_name='Номер дома',
        max_length=255,
        null=True,
        blank=True,
    )

    opening_time = models.TimeField(
        "Время открытия",
        blank=True,
    )

    closing_time = models.TimeField(
        "Время закрытия",
        blank=True,
    )


    class Meta:
        db_table = 'shop'
        verbose_name = 'Магазины'
        verbose_name_plural = 'Магазин'
        ordering = ['name', ]

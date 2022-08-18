from django.db import models

class Shop(models.Model):
    """Модель Магазина"""

    name = models.CharField(
        verbose_name='Название магазина',
        max_length=256,
        null=False,
        blank=True,
    )
    
    town = models.ForeignKey()
    street = models.ForeignKey()
    
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

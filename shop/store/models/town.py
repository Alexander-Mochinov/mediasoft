from django.db import models


class Town(models.Model):
    """Модель города"""

    name = models.CharField(
        verbose_name='Название города',
        max_length=256,
        null=False,
        blank=True,
    )
    
    class Meta:
        db_table = 'town'
        verbose_name = 'Города'
        verbose_name_plural = 'Город'
        ordering = ['name', ]

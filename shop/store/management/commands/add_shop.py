from random import choice
from datetime import time

from django.core.management.base import BaseCommand

from store.models import Shop, Town, Street


class Command(BaseCommand):
    
    help = 'Добавление магазина'

    def handle(self, *args, **options):
        try:
            shop_name = [
                'ikea',
                'mvidio',
                'dns',
                'achan',
                'el darada',
            ]
            for shop in shop_name:
                Shop.objects.create(
                    name=shop,
                    town=choice(Town.objects.all()),
                    street=choice(Street.objects.all()),
                    house=choice(['1', '3', '5', '7', '10', '11', '15']),
                    opening_time=time(8, 0),
                    closing_time=time(16, 0),
                )

            self.stdout.write(self.style.SUCCESS('Магазины добавленны'))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Что то пошло не так :('))
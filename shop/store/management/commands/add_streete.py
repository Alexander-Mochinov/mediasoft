from random import choice

from django.core.management.base import BaseCommand

from store.models import Street, Town


class Command(BaseCommand):

    help = 'Добавление улицы'

    def handle(self, *args, **options):
        try:

            list_street = [
                "1-я Рядовая",
                "1-я Угловая",
                "2-я Бригадная",
                "Баженова",
                "Балкыш",
                "Баллы",
                "Газовая",
                "Груздева",
                "Желатиновая",
                "Зайцева",
                "Залесная",
                "Знатная",
            ]
            
            for street in list_street:
                Street.objects.create(
                    name=street,
                    town=choice(Town.objects.all())
                )
            self.stdout.write(self.style.SUCCESS('Улицы добавленны'))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Что то пошло не так :('))

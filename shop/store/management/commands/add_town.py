from django.core.management.base import BaseCommand

from store.models import Town


class Command(BaseCommand):
    
    help = 'Добавление городов'

    def handle(self, *args, **options):
        try:
            list_town = [
                "Анапа",
                "Анива",
                "Ардон",
                "Аша",
                "Бавлы",
                "Баймак",
                "Барнаул",
                "Белгород",
                "Белово",
                "Богородск",
                "Боровск",
                "Бузулук",
                "Валдай",
                "Видное",
                "Гаджиево",
                "Москва",
                "Самара",
                "Калининград",
                "Омск",
            ]
            
            for town in list_town:
                Town.objects.create(
                    name=town,
                )
            self.stdout.write(self.style.SUCCESS('Города добавленны'))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS('Что то пошло не так :('))

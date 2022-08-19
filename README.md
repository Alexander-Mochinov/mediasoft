# mediasoft

Создайте виртуальное окружение и установите зависимости
pip install -r requirements.txt

Выполнить команды по порядку

```python
./manage.py makemigrations
./manage.py migrate
./manage.py add_town
./manage.py add_streete
./manage.py add_shop
```

Endpoints
```python

admin/
api-auth/
api/v1/ shop/ 
api/v1/ city/ 
api/v1/ city/<town_id>/street/
```


Задание:
Реализовать сервис, который принимает и отвечает на HTTP запросы.

Функционал
В случае успешной обработки сервис должен
отвечать статусом 200, в случае любой ошибки — статус 400.
Сохранение всех объектов в базе данных.
Запросы
 GET /city/—получениевсехгородовизбазы;
 GET /city//street/—получение всех улиц города; (city_id — идентификатор города)
 POST /shop/—создание магазина;
Данный метод получает json c объектом магазина, в ответ возвращает id созданной записи.
GET/shop/?street=&city=&open=0/1
получение списка магазинов;
i. Метод принимает параметры для фильтрации. 
    Параметры не обязательны. В случае отсутствия параметров выводятся все магазины, если хоть один параметр есть , то по нему выполняется фильтрация.
ii. Важно! 
    в объекте каждого магазина выводится название города и улицы, а не id записей.
iii. Параметр open: 0 - закрыт, 1 - открыт. 
    Данный статус определяется исходя из параметров «Время открытия», «Время закрытия» и текущего времени сервера.

Объекты: Магазин:
    Названи Город
    Улица
    Дом
    Время открытия 
    Время закрытия

Город:
    Название

Улица:
    Название
    Город

!! Замечание: поле id у объектов не указаны, но подразумевается что они есть.
!! Важно: Выстроить связи между таблицами в базе данных.

Инструменты:
Фреймворк для обработки http запросов Django, Django Rest Framewor
Реляционная БД (PostgreSQL-предпочтительно, MySQL и тд)
Запросы в базу данных через ORM (ORM навыбор).
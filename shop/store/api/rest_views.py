from datetime import time
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from store.api.serializers import (
    ShopSerializer,
    StreetSerializer,
    TownSerializer,
)
from store.models import (
    Shop,
    Street,
    Town,
)


@api_view(['GET',])
def town_list(request):
    """
    Список всех городов
    """

    if request.method == 'GET':
        towns = Town.objects.all()
        serializer = TownSerializer(towns, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET',])
def street_list(request, town_id):
    """
    Список всех улиц исходя из ID города
    """

    if request.method == 'GET':
        street = Street.objects.filter(town__id = town_id)
        serializer = StreetSerializer(street, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def shop(request):
    """
    Получение списка магазинов по фильтрации и создание
    """

    if request.method == 'GET':
        open_time = request.GET.get('open', 0)
        query = {
            'street__name__icontains': request.GET.get('street', ''),
            'town__name__icontains': request.GET.get('city', ''),
            'opening_time__lt': time(8, 0) if int(open_time) else time(16, 0),
            'closing_time__gt': time(16, 0) if int(open_time) else time(8, 0),
        }
        shop = Shop.objects.filter(**query)
        serializer = ShopSerializer(shop, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    if request.method == 'POST':
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
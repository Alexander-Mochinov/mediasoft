from rest_framework import serializers

from store.models import (
    Shop,
)


class ShopSerializer(serializers.ModelSerializer):
    town = serializers.ReadOnlyField(source='town.name')
    street = serializers.ReadOnlyField(source='street.name')
    
    class Meta:
        model = Shop
        fields = [
            "name", "town", "street", "house", "opening_time", "closing_time",
        ]

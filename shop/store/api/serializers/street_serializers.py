from rest_framework import serializers

from store.models import (
    Street
)


class StreetSerializer(serializers.ModelSerializer):

    town = serializers.ReadOnlyField(source='town.name')
    
    class Meta:
        model = Street
        fields = [
            "name", "town",
        ]

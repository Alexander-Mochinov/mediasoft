from rest_framework import serializers

from store.models import (
    Town,
)


class TownSerializer(serializers.ModelSerializer):

    class Meta:
        model = Town
        fields = [
            "name",
        ]

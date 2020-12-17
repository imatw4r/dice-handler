from rest_framework import serializers
from dice.models import Dice


class DiceSerializer(serializers.ModelSerializer):
    faces = serializers.IntegerField(min_value=0, max_value=1000)

    class Meta:
        model = Dice
        fields = ("name", "faces", "created", "updated")
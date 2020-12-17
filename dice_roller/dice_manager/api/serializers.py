from rest_framework import serializers
from dice_manager.models import DiceManager


class DiceManagerSerializer(DiceManagerListSerializer):
    roll = serializers.SerializerMethodField("dice_roll")

    class Meta:
        model = DiceManager
        fields = ("name", "created", "updated", "dice", "url", "roll")
        list_serializer_class = DiceManagerListSerializer

    def dice_roll(self, instance):
        return sum((dice.roll() for dice in instance.dice.all()))

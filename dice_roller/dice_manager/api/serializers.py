from rest_framework import serializers
from dice_manager.models import DiceManager


class DiceManagerSerializer(serializers.HyperlinkedModelSerializer):
    roll = serializers.SerializerMethodField("dice_roll")

    class Meta:
        model = DiceManager
        fields = ("name", "created", "updated", "dice", "url", "roll")

    def dice_roll(self, instance):
        return sum((dice.roll() for dice in instance.dice.all()))

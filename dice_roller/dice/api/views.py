from rest_framework.viewsets import ModelViewSet

from dice.models import Dice
from dice.api.serializers import DiceSerializer


class DiceViewSet(ModelViewSet):
    queryset = Dice.objects.all()
    serializer_class = DiceSerializer

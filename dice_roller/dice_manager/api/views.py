from rest_framework.viewsets import ModelViewSet

from dice_manager.models import DiceManager
from dice_manager.api.serializers import DiceManagerSerializer


class DiceManagerViewSet(ModelViewSet):
    queryset = DiceManager.objects.prefetch_related("dice")
    serializer_class = DiceManagerSerializer

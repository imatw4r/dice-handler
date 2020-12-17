from rest_framework.routers import DefaultRouter
from dice_manager.api.views import DiceManagerViewSet

router = DefaultRouter()

router.register("dicehandle", DiceManagerViewSet)

app_name = "Dice Handler"
urlpatterns = router.urls

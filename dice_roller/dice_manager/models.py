from django.db import models
from dice.models import Dice


class DiceManager(models.Model):
    name = models.CharField(max_length=50, unique=True)
    dice = models.ManyToManyField(Dice, blank=False)
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated = models.DateTimeField(auto_now_add=True, auto_created=True)

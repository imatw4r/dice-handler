from django.db import models
import random


class Dice(models.Model):
    name = models.CharField(max_length=50, unique=True)
    faces = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated = models.DateTimeField(auto_now_add=True, auto_created=True)

    def roll(self):
        return random.randint(0, self.faces)

    def __str__(self):
        return self.name
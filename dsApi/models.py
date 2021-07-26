from django.db import models
from django.db.models.base import Model

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.FloatField(max_length=6)
    age = models.IntegerField()

    def __str__(self):
        return self.name

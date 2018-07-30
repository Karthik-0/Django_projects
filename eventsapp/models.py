from django.db import models
from model_utils.models import TimeStampedModel
from placesapp.models import Place


# class Event(Place, TimeStampedModel):
#     title = models.CharField(max_length=50)
#     place = models.ManyToManyField("Place")
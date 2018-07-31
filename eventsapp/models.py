from django.db import models
from model_utils.models import TimeStampedModel
from taggit.managers import TaggableManager


class Event(TimeStampedModel):
    title = models.CharField(max_length=50)
    place = models.ForeignKey("placesapp.Place", on_delete=models.CASCADE)
    tags = TaggableManager()

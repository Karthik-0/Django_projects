from django.contrib.gis.db import models
from taggit.managers import TaggableManager


class PlaceType(models.Model):
    places = models.CharField(max_length=30)

    def __str__(self):
        return self.places


class Place(models.Model):
    title = models.CharField(max_length=50)
    location = models.PointField()
    desc = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    tags = TaggableManager()
    placetypes = models.ManyToManyField("PlaceType")

    def __str__(self):
        return self.title

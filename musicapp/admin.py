from django.contrib import admin
from .models import Musician, Album, Band, Label, Genre, Track

myModels = [Musician, Album, Band, Label, Genre, Track]
admin.site.register(myModels)

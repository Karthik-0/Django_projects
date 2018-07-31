from django.contrib import admin
from .models import Movie, Director, Studio, Genre


admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Studio)
admin.site.register(Genre)

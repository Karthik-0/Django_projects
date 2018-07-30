from django.contrib import admin
from .models import Place, PlaceType

admin.site.register(Place)
admin.site.register(PlaceType)
# class MarkerAdmin(admin.OSMGeoAdmin):
#     default_lon = -93
#     default_lat = 27
#     default_zoom = 15
#     readonly_fields = ('Latitude','Longitude')
# admin.site.register(Marker, MarkerAdmin)

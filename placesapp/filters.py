import django_filters
from .models import Place


class PlaceFilter(django_filters.FilterSet):
    class Meta:
        model = Place
        fields = ['city']

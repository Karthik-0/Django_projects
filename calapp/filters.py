import django_filters
from .models import Entry


class DateFilter(django_filters.FilterSet):
    year = django_filters.NumberFilter(
        field_name='date__year',
        lookup_expr='exact')
    day = django_filters.NumberFilter(
        field_name='date__day',
        lookup_expr='exact')
    month = django_filters.NumberFilter(
        field_name='date__month',
        lookup_expr='exact')

    class Meta:
        model = Entry
        fields = ['year', 'day', 'month']

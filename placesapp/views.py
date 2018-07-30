from django.views import generic
from .models import Place
from . import forms
from .filters import PlaceFilter


class PlaceList(generic.ListView):
    template_name = 'index.html'
    model = Place
    filterset_class = PlaceFilter
    context_object_name = 'places'

    def get_context_data(self, **kwargs):
        places = Place.objects.all()
        # tags = books.values_list('genre__name',flat=True).distinct()
        data = super().get_context_data(**kwargs)
        filter = PlaceFilter(self.request.GET, queryset=places)
        # print(filter.qs)
        cities = places.values_list('city', flat=True).distinct()
        data['filteredplaces'] = filter
        data['cities'] = cities
        print(places.values_list('city', flat=True).values().distinct())
        # data['tags'] = tags
        # print(data['filteredbooks'])
        return data


class PlaceDetail(generic.DetailView):
    template_name = 'detail.html'
    model = Place
    context_object_name = 'place'

    def get_object(self, queryset=None):
        obj = super(PlaceDetail, self).get_object(queryset=queryset)
        print(obj.location.coords)
        return obj


class PlaceCreate(generic.CreateView):
    template_name = 'add.html'
    model = Place
    success_url = '/places'
    # fields = ['title','desc','location']
    form_class = forms.PlaceForm

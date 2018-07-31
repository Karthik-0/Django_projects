from django.views import generic
from .models import Movie


class MovieListView(generic.ListView):
    model = Movie
    template_name = "movies/index.html"
    context_object_name = 'movies'


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "movies/detail.html"
    context_object_name = 'movie'

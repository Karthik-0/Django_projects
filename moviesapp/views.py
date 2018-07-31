from django.views import generic
from .models import Movie


class MovieListView(generic.ListView):
    model = Movie
    template_name = "movies/index.html"

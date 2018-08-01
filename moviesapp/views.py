from django.views import generic
from .models import Movie, Genre, Director, Studio


class MovieListView(generic.ListView):
    model = Movie
    template_name = "movies/index.html"
    context_object_name = 'movies'


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "movies/detail.html"
    context_object_name = 'movie'


class StudioListView(generic.ListView):
    model = Studio
    template_name = "movies/studioindex.html"
    context_object_name = 'studios'


class StudioDetailView(generic.DetailView):
    model = Studio
    template_name = "movies/studiodetail.html"
    context_object_name = 'studio'


class DirectorListView(generic.ListView):
    model = Director
    template_name = "movies/directorindex.html"
    context_object_name = 'directors'


class DirectorDetailView(generic.DetailView):
    model = Director
    template_name = "movies/directordetail.html"
    context_object_name = 'director'


class GenreListView(generic.ListView):
    model = Genre
    template_name = "movies/genreindex.html"
    context_object_name = 'genres'


class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = "movies/genredetail.html"
    context_object_name = 'genre'

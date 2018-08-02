from django.views import generic
from .models import Album, Track, Band, Label


class AlbumList(generic.ListView):
    template_name = "music/index.html"
    model = Album
    context_object_name = 'albums'


class AlbumDetail(generic.DetailView):
    template_name = "music/detail.html"
    model = Album
    context_object_name = 'album'


class SongList(generic.ListView):
    template_name = "music/songlist.html"
    model = Track
    context_object_name = 'tracks'


class SongDetail(generic.DetailView):
    template_name = "music/songdetail.html"
    model = Track
    context_object_name = 'track'


class BandList(generic.ListView):
    template_name = "music/bandlist.html"
    model = Band
    context_object_name = 'bands'


class BandDetail(generic.DetailView):
    template_name = "music/banddetail.html"
    model = Band
    context_object_name = 'band'


class LabelList(generic.ListView):
    template_name = "music/labellist.html"
    model = Label
    context_object_name = 'labels'


class LabelDetail(generic.DetailView):
    template_name = "music/labeldetail.html"
    model = Label
    context_object_name = 'label'

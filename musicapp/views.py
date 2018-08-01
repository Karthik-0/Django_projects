from django.views import generic
from .models import Album, Track


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

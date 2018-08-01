from django.views import generic
from .models import Album


class MusicList(generic.ListView):
    template_name = "music/index.html"
    model = Album
    context_object_name = 'albums'

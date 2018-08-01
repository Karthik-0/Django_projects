from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.AlbumList.as_view(), name="index"),
    path('detail/<slug>', views.AlbumDetail.as_view(), name="detail"),
    path('songs/', views.SongList.as_view(), name="song_index"),
    path('song/detail/<slug>', views.SongDetail.as_view(), name="song_detail"),
]

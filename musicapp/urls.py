from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.AlbumList.as_view(), name="album_list"),
    path('songs/', views.SongList.as_view(), name="song_list"),
    path('detail/<slug>', views.AlbumDetail.as_view(), name="album_detail"),
    path('bands/', views.BandList.as_view(), name="band_list"),
    path('band/detail/<int:pk>', views.BandDetail.as_view(),
         name="band_detail"),
    path('song/detail/<slug>', views.SongDetail.as_view(), name="song_detail"),
]

from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.MusicList.as_view(), name="index"),
]

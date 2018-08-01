from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='index'),
    path('studio/', views.StudioListView.as_view(), name='studioindex'),
    path('studio/<slug>/', views.StudioDetailView.as_view(),
         name='studiodetail'),
    path('director/', views.DirectorListView.as_view(), name='directorindex'),
    path('director/<int:pk>/', views.DirectorDetailView.as_view(),
         name='directordetail'),
    path('genre/', views.GenreListView.as_view(), name='genreindex'),
    path('genre/<slug>/', views.GenreDetailView.as_view(), name='genredetail'),
    path('<slug>/', views.MovieDetailView.as_view(), name='detail'),
]

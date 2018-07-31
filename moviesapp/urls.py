from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MovieListView.as_view(), name='index'),
    path('<slug>/', views.MovieDetailView.as_view(), name='detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlaceList.as_view(), name="index"),
    path('<int:pk>/', views.PlaceDetail.as_view(), name="detail"),
    path('add/', views.PlaceCreate.as_view(), name="add")
]

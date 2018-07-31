from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login', auth_views.login, name="login"),
    path('logout', auth_views.logout, name="logout"),
    path('signup', views.signup, name="signup"),
    path('entry/<int:pk>', views.details, name="details"),
    path('entry/add', views.add, name="add"),
    path('dashboard/entry/delete/<int:pk>', views.delete, name="delete"),
]

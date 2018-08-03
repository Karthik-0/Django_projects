from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.ForumIndex.as_view(), name="index"),
    path('post/<slug>', views.PostDetails.as_view(), name="post_detail"),
]

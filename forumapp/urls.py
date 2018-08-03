from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.ForumIndex.as_view(), name="index"),
    path('post/<slug>', views.PostDetails.as_view(), name="post_detail"),
    path('thread/<slug>', views.ThreadDetail.as_view(), name="thread_detail"),
    path("login/", auth_views.login,
         {'template_name': 'forum/registration/login.html'}, name="login"),
    path('logout/', auth_views.logout, {'next_page': '/forum'}, name="logout"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('comment/', views.CommentBox.as_view(), name="comment")

]

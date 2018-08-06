from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.ForumIndex.as_view(), name="index"),
    path('post/create/', views.PostCreate.as_view(), name="create_post"),
    path('post/edit/<slug>', views.PostEdit.as_view(), name="edit_post"),
    path('post/delete/<slug>', views.PostDelete.as_view(), name="delete_post"),
    path('thread/create/', views.ThreadCreate.as_view(), name="create_thread"),
    path('thread/<slug>', views.ThreadDetail.as_view(), name="thread_detail"),
    path("login/", auth_views.login,
         {'template_name': 'forum/registration/login.html'}, name="login"),
    path('logout/', auth_views.logout, {'next_page': '/forum'}, name="logout"),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password/change/', views.change_password, name='change_password'),
    path('comment/', views.CommentBox.as_view(), name="comment"),
    path('comment/edit/<int:pk>',
         views.CommentEdit.as_view(), name="edit_comment"),
    path('comment/delete/<int:pk>',
         views.CommentDelete.as_view(), name="delete_comment"),
    path('post/<slug>', views.PostDetails.as_view(), name="post_detail"),
]

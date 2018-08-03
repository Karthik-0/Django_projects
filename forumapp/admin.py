from django.contrib import admin
from .models import User, Thread, Post, Comment
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username']


admin.site.register(User)
admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(Comment)

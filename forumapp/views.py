from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .decorators import moderator_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post, Thread, Comment, User
from .forms import CustomUserCreationForm


# @method_decorator(moderator_required, name='dispatch')
class ForumIndex(generic.ListView):
    model = Post
    template_name = "forum/index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(ForumIndex, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.all()
        sort = self.request.GET.get('sort', None)
        sorts = {
            'oldest': '-created',
            'title': 'title',
            'reverse': '-title',
            'latest': '-modified'
        }
        if sort is None:
            print("No sort")
            context['sort'] = 'latest'
            context['sortvalue'] = sorts['latest']
        else:
            context['sort'] = sort
            context['sortvalue'] = sorts[sort]
        return context


class PostDetails(generic.DetailView):
    template_name = "forum/post_detail.html"
    model = Post
    context_object_name = "post"


class ThreadDetail(generic.DetailView):
    template_name = "forum/thread_detail.html"
    model = Thread
    context_object_name = "thread"


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('forum:login')
    template_name = 'forum/registration/signup.html'


class CommentBox(LoginRequiredMixin, generic.CreateView):
    model = Comment
    template_name = "forum/_comment_box.html"
    fields = ['user', 'content', 'post']

    def post(self, request, *args, **kwargs):
        post_slug = request.POST.get("post", "")
        content = request.POST.get("content", "")
        bar = Comment.objects.create(
            post_id=post_slug,
            user=request.user,
            content=content)
        bar.save()
        url = reverse('forum:post_detail', kwargs={'slug': post_slug})
        return HttpResponseRedirect(url)


class PostCreate(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'forum/createpost.html'
    fields = ['title', 'content', 'thread', 'user']

    def get_success_url(self, *args, **kwargs):
        return reverse('forum:post_detail', kwargs={'slug': self.object.slug})


class ThreadCreate(LoginRequiredMixin, generic.CreateView):
    model = Thread
    template_name = 'forum/createthread.html'
    fields = ['title', 'subject', 'user']

    def get_success_url(self, *args, **kwargs):
        return reverse('forum:thread_detail',
                       kwargs={'slug': self.object.slug})


class PostEdit(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = "forum/createpost.html"
    fields = ['title', 'content', 'thread', 'user']

    def get_queryset(self):
        base_qs = super(PostEdit, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def get_success_url(self, *args, **kwargs):
        return reverse('forum:post_detail', kwargs={'slug': self.object.slug})


class PostDelete(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('forum:index')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class CommentEdit(generic.UpdateView):
    model = Comment
    template_name = "forum/edit_comment.html"
    fields = ['user', 'content', 'post']

    def get_success_url(self, *args, **kwargs):
        print(self.object)
        return reverse('forum:post_detail',
                       kwargs={'slug': self.object.post.slug})


class CommentDelete(generic.DeleteView):
    model = Comment

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    def get_success_url(self):
        post = self.object.post
        return reverse_lazy('forum:post_detail', kwargs={'slug': post.slug})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request,
                             'Your password was successfully updated!')
            return redirect('forum:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'forum/registration/change_password.html', {
        'form': form
    })


@method_decorator(moderator_required, name='dispatch')
class ThreadDelete(generic.DeleteView):
    model = Thread
    success_url = reverse_lazy('forum:index')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


@method_decorator(staff_member_required, name="dispatch")
class UserList(generic.ListView):
    model = User
    template_name = "forum/registration/user_list.html"
    context_object_name = "users"


class UserEdit(generic.View):

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get("user_id", "")
        bar = User.objects.get(pk=user_id)
        bar.is_moderator = True
        bar.save()
        messages.success(request, 'Operation Successfull.')
        url = reverse('forum:index')
        return HttpResponseRedirect(url)
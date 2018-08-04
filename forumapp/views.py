from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Post, Thread, Comment
from .forms import CustomUserCreationForm


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
            'latest': 'modified'
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

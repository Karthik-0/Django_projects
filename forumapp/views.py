from django.views import generic
from django.urls import reverse_lazy, reverse
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
    success_url = reverse_lazy('login')
    template_name = 'forum/registration/signup.html'


class CommentBox(generic.CreateView):
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
        return HttpResponseRedirect('/forum/post/%s' % post_slug)


class PostCreate(generic.CreateView):
    model = Post
    template_name = 'forum/createpost.html'
    fields = ['title', 'content', 'thread', 'user']

    def get_success_url(self, *args, **kwargs):
        return reverse('forum:post_detail', kwargs={'slug': self.object.slug})


class ThreadCreate(generic.CreateView):
    model = Thread
    template_name = 'forum/createthread.html'
    fields = ['title', 'subject', 'user']

    def get_success_url(self, *args, **kwargs):
        return reverse('forum:thread_detail',
                       kwargs={'slug': self.object.slug})

from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Post, Thread, Comment, User
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


class CommentBox(generic.View):
    model = Comment
    template_name = "forum/_comment_box.html"
    fields = ['user', 'content', 'post']

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get("user", "")
        post_slug = request.POST.get("post", "")
        content = request.POST.get("content", "")
        # print(post_slug)
        posts = Post.objects.get(pk=str(post_slug))
        # print(posts)
        user = User.objects.get(pk=user_id)
        # print(user)
        bar = Comment.objects.create(
            post=posts,
            user=user,
            content=content)
        bar.save()
        return HttpResponseRedirect('/forum/post/%s' % post_slug)

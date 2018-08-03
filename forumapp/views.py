from django.views import generic
from django.urls import reverse_lazy
from .models import Post, Thread
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

from django.views import generic
from .models import Post, Thread


class ForumIndex(generic.ListView):
    model = Post
    template_name = "forum/index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super(ForumIndex, self).get_context_data(**kwargs)
        context['threads'] = Thread.objects.all()
        return context

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from .utils import get_unique_slug
from model_utils.models import TimeStampedModel


class Thread(TimeStampedModel):
    title = models.CharField(max_length=50, unique=True)
    subject = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True,
                            primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="threads")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Post(TimeStampedModel):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(blank=True, primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="posts")
    thread = models.ForeignKey(Thread,
                               on_delete=models.CASCADE,
                               related_name="posts")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'title', 'slug')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.slug})


class Comment(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name="comments")
    post = models.ForeignKey("Post", on_delete=models.CASCADE,
                             related_name="comments")
    content = models.TextField()

    def __str__(self):
        return self.content

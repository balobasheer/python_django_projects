from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import User


# Create your models here.

class HidePostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=True)


class ShowPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=False)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    is_hidden = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = models.Manager()
    deleted_object = HidePostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)

    objects = models.Manager()
    deleted_object = HidePostManager()
    active_object = ShowPostManager()

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('post-detail', args=(str(self.pk)))


class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(CommentPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




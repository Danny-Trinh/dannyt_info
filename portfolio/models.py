from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    link = models.TextField()
    picture = models.ImageField(default='project_default.jpg', upload_to='project_pics')

    def __str__(self):
        return self.title


class ForumPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


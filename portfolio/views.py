from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)
from .models import Project, ForumPost
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User


# this is the "home view"
class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/home.html'
    paginate_by = 2
    ordering = '-date_posted'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Homepage"
        context["home"] = True
        return context


class UserPostListView(ListView):
    model = ForumPost
    template_name = 'portfolio/forums.html'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return ForumPost.objects.filter(author=user).order_by('-date_posted')


class PostListView(ListView):
    model = ForumPost
    template_name = 'portfolio/forums.html'
    paginate_by = 2
    ordering = '-date_posted'


# without setting template_name, this class auto-looks for template blog/post_detail
class PostDetailView(DetailView):
    model = ForumPost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = ForumPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = ForumPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ForumPost
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


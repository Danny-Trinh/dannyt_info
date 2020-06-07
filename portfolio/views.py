from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)
from .models import Project, ForumPost, Resume
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
        context["title"] = "Danny Trinh"
        context["home"] = True
        context["resume"] = Resume.objects.first()
        return context


class UserPostListView(ListView):
    model = ForumPost
    template_name = 'portfolio/forums.html'
    paginate_by = 8

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return ForumPost.objects.filter(author=user).order_by('-date_posted')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        context["title"] = "@" + user.username
        return context


class PostListView(ListView):
    model = ForumPost
    template_name = 'portfolio/forums.html'
    paginate_by = 4
    ordering = '-date_posted'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User Posts"
        return context


# without setting template_name, this class auto-looks for template blog/post_detail
class PostDetailView(DetailView):
    model = ForumPost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User Post"
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = ForumPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Post"
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = ForumPost
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Post"
        return context


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ForumPost
    success_url = '/forums'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Post"
        return context


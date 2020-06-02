from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView,
                                  UpdateView)
from .models import Project



# def home(request):
#     return render(request, 'portfolio/home.html', {'title': 'My Projects', 'home': True})


def forums(request):
    return render(request, 'portfolio/forums.html', {'title': 'Forums'})


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


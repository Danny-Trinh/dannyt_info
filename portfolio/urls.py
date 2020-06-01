from . import views
from django.urls import path
urlpatterns = [
    # path('', views.home, name='home'),
    path('forums', views.forums, name='forums'),
    path('', views.ProjectListView.as_view(), name='home'),
]

from . import views
from django.urls import path
urlpatterns = [
    path('forums/', views.PostListView.as_view(), name='forums'),
    path('', views.ProjectListView.as_view(), name='home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete')
]

from . import views
from django.urls import path
urlpatterns = [
    path('pokemon/', views.pokemon_view, name='pokehome'),
]

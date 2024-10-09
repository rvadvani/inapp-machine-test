# api/urls.py
from django.urls import path
from .views import LoginView, MovieSearchView, PersonSearchView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('search-movies/', MovieSearchView.as_view(), name='search_movies'),
    path('search-person/', PersonSearchView.as_view(), name='search-person'),
]

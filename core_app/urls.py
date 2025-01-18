from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies', views.movies, name = 'Movies List')
    # Add more paths here
]
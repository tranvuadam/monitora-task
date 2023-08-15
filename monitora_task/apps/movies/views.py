from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from monitora_task.apps.movies.models import Movie


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie_detail.html"
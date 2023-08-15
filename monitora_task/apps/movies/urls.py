from django.urls import path

from monitora_task.apps.movies.views import MovieDetailView

app_name = 'movies'

urlpatterns = [
    path("<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
]

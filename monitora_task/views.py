from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView
from unidecode import unidecode

from monitora_task.apps.actors.models import Actor
from monitora_task.apps.movies.models import Movie


class HomeView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", None)
        # use prefetch_related if many to many relations are needed in template/used
        movie_qs = Movie.objects.all()
        actor_qs = Actor.objects.all()
        if name:
            unaccent_name = unidecode(name)
            movie_qs = movie_qs.filter_unaccent_name(unaccent_name)
            actor_qs = actor_qs.filter_unaccent_name(unaccent_name)
        context["movies"] = movie_qs
        context["actors"] = actor_qs
        context["query"] = name or ""
        return context



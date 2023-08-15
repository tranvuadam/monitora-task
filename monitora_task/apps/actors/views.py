from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView

from monitora_task.apps.actors.models import Actor


class ActorDetailView(DetailView):
    model = Actor
    template_name = "actor_detail.html"

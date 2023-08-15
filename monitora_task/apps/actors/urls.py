from django.urls import path

from monitora_task.apps.actors.views import ActorDetailView
app_name = 'actors'

urlpatterns = [
    path("<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
]

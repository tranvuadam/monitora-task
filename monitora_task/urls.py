from django.contrib import admin
from django.urls import path, include

from monitora_task.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('actors/', include('monitora_task.apps.actors.urls')),
    path('movies/', include('monitora_task.apps.movies.urls')),
    path('admin/', admin.site.urls),
]

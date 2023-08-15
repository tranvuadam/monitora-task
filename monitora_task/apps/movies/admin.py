from django.contrib import admin

# Register your models here.
from monitora_task.apps.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass

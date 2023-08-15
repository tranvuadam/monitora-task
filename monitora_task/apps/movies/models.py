from django.db import models

# Create your models here.
from django.utils.translation import gettext as _

from monitora_task.apps.movies.managers import MovieManager


class Movie(models.Model):
    name = models.CharField(_("name"), max_length=1023)
    unaccent_name = models.CharField(_("unaccent_name"), max_length=1023)
    actors = models.ManyToManyField("actors.Actor", related_name="movies")

    objects = MovieManager.as_manager()

    class Meta:
        verbose_name = _("movie")
        verbose_name_plural = _("movies")

    def __str__(self):
        return self.name

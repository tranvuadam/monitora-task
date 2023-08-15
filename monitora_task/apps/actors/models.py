from django.db import models

# Create your models here.
from django.utils.translation import gettext as _

from monitora_task.apps.actors.managers import ActorManager


class Actor(models.Model):
    name = models.CharField(_("name"), max_length=1023)
    unaccent_name = models.CharField(_("unaccent_name"), max_length=1023)

    objects = ActorManager.as_manager()

    class Meta:
        verbose_name = _("actor")
        verbose_name_plural = _("actors")

    def __str__(self):
        return self.name

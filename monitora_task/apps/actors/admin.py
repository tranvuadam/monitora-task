from django.contrib import admin

# Register your models here.
from monitora_task.apps.actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass

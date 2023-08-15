from django.db import models


class MovieManager(models.QuerySet):
    def filter_unaccent_name(self, unaccent_name: str):
        return self.filter(unaccent_name__icontains=unaccent_name)

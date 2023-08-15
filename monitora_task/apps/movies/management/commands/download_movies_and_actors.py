import requests
from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup

from monitora_task.apps.actors.models import Actor
from monitora_task.apps.movies.models import Movie
from unidecode import unidecode


class Command(BaseCommand):
    actor_names = {}
    headers = {'User-agent': 'Chrome/115.0.0.0 Safari/537.36'}

    def process_film_detail(self, url: str):
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.content, "html.parser")
        creators = soup.find("div", class_="creators").find("h4", string="Hrají:")
        actors = creators.parent.find_all("a", class_=None) if creators else []
        result = []
        for actor in actors:
            actor_name = actor.text.strip()
            if actor_name not in self.actor_names:
                actor = Actor(name=actor_name, unaccent_name=unidecode(actor_name))
                actor.save()
                self.actor_names[actor_name] = actor
            result.append(self.actor_names[actor_name])
        return result

    def handle(self, *args, **options):
        from_params = ["1", "100", "200"]
        BASE_URL = "https://www.csfd.cz/"
        csfd_top_movies_url = BASE_URL + "zebricky/filmy/nejlepsi/?from="
        for param in from_params:
            url = csfd_top_movies_url + param
            page = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(page.content, "html.parser")
            job_elements = soup.find_all("article", class_="article")

            for job_element in job_elements:
                name = job_element.find("a", class_="film-title-name")
                film_detail_url = BASE_URL + name["href"]
                actors = self.process_film_detail(film_detail_url)
                movie_name = name.text.strip()
                movie = Movie(name=movie_name, unaccent_name=unidecode(movie_name))
                movie.save()
                movie.actors.set(actors)

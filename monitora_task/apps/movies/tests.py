from django.test import TestCase

# Create your tests here.
from unidecode import unidecode

from monitora_task.apps.movies.models import Movie


class TestMovieManager(TestCase):
    def test_filter_unaccent(self):
        m = Movie.objects.create(name="čžc", unaccent_name=unidecode("čžc"))
        m2 = Movie.objects.create(name="abc", unaccent_name=unidecode("abc"))

        self.assertEqual(m, Movie.objects.filter_unaccent_name("czc").first())

    def test_filter_unaccent_substring(self):
        m = Movie.objects.create(name="yyčžcxx", unaccent_name=unidecode("yyčžcxx"))
        m2 = Movie.objects.create(name="abc", unaccent_name=unidecode("abc"))

        self.assertEqual(m, Movie.objects.filter_unaccent_name("czc").first())

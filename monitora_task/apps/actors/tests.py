from django.test import TestCase

# Create your tests here.
from monitora_task.apps.actors.models import Actor
from unidecode import unidecode


class TestActorManager(TestCase):
    def test_filter_unaccent(self):
        m = Actor.objects.create(name="čžc", unaccent_name=unidecode("čžc"))
        m2 = Actor.objects.create(name="abc", unaccent_name=unidecode("abc"))

        self.assertEqual(m, Actor.objects.filter_unaccent_name("czc").first())

    def test_filter_unaccent_substring(self):
        m = Actor.objects.create(name="yyčžcxx", unaccent_name=unidecode("yyčžcxx"))
        m2 = Actor.objects.create(name="abc", unaccent_name=unidecode("abc"))

        self.assertEqual(m, Actor.objects.filter_unaccent_name("czc").first())

from django.test import TestCase
from django.utils import timezone
from .models import Episod

# Create your tests here.
class PodCastsTests(TestCase):
    def setUp(self) -> None:
        self.episode = Episod.objects.create(
            title = 'My nice podcast Episode',
            description = 'Django new features in version',
            pub_date = timezone.now(),
            link = 'https://myawesomeshow.com',
            image='https://image.myawesomeshow.com',
            podcast_name="My Python Podcast",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr",)

    def test_episode_content(self):
        self.assertEqual(self.episode.description, 'Django new features in version'),
        self.assertEqual(self.episode.link, 'https://myawesomeshow.com'),
        self.assertEqual(self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"),

    def test_episode_str_representation(self):
        self.assertEqual(str(self.episode), "My Python Podcast: My Awesome Podcast Episode")
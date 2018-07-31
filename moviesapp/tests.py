from django.test import TestCase
from moviesapp.models import Movies,Comments
from rest_framework import status
from moviesapp.serializers import MoviesSerializer,CommentsSerializer


class Mtest(TestCase):

    def setUp(self):
        Movies.objects.create(
            title='Spider-man', year='2002', director='Stan Lee')

    def test_movie(self):
        x_movie = Movies.objects.get(title='Spider-man')

        self.assertEqual(
            x_movie.year_dir(), 'Movie Spider-man was made in 2002 by Stan Lee')


class MoviesTest(TestCase):
    def setUp(self):
        self.movie_attributes = {
            'title': 'Batman',
            'year': '2007'
        }

        self.serializer_data = {
            'title': 'Superman',
            'year': '2008'
        }

        self.movie = Movies.objects.create(**self.movie_attributes)
        self.serializer = MoviesSerializer(instance=self.movie)

    def test_serial(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()), set({'title', 'year', 'actors',
                                                'imdb_id',
                                                'director',
                                                'production',
                                                'rated',
                                                'country',
                                                'writer',
                                                'ratings',
                                                'genre',
                                                'awards',
                                                'boxoffice',
                                                'language',
                                                'plot',
                                                'type',
                                                'website',
                                                'poster',
                                                'runtime',
                                                'dvd',
                                                'imdb_votes',
                                                'response',
                                                'metascore',
                                                'id',
                                                'imdb_rating',
                                                'released'}))
    def test_all_movies_view(self):
        response = self.client.get('/root/all_movies/')
        self.assertEqual(response.status_code, 200)

class CommSerialTest(TestCase):
    def setUp(self):
        self.comment_attributes = {
            'comment': 'nice movie',
            'commented_movie': Movies.objects.create()
        }

        self.serializer_data = {
            'comment': 'bad movie',
            'commented_movie': Movies.objects.create()
        }

        self.comment = Comments.objects.create(**self.comment_attributes)
        self.serializer = CommentsSerializer(instance=self.comment)

    def test_serial(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'commented_movie','comment']))
    def test_all_comments_view(self):
        response = self.client.get('/root/all_comments/')
        self.assertEqual(response.status_code, 200)

    def test_post_comment(self):
        data={'comment':'some comment','commented_movie': Movies.objects.create()}
        url='/root/add_comment'
        response=self.client.post(url,data,follow=True)
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)




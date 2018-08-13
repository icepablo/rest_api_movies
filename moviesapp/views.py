import requests

from .serializers import MoviesSerializer, CommentsSerializer, AddSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import generics, status, viewsets

from moviesapp.models import Movies, Comments


class CommentsList(viewsets.ViewSetMixin, generics.ListAPIView):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['commented_movie']


class AddComment(viewsets.ViewSetMixin, generics.CreateAPIView):
    serializer_class = CommentsSerializer


class MoviesList(viewsets.ViewSetMixin, generics.ListAPIView):
    serializer_class = MoviesSerializer
    queryset = Movies.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filter_fields = ['title', 'id', 'year', 'imdb_id', 'type']


class AddTitle(generics.CreateAPIView):
    serializer_class = AddSerializer

    def post(self, request):
        if request.method == 'POST':
            post_title=request.data['add']
            url = 'http://www.omdbapi.com/?t=' + post_title + '&apikey=b3bdacd8'
            json_object = requests.post(url)
            if json_object.status_code == 200:
                json_object = requests.post(url).json()
                all_movies = Movies.objects.all()
                try:
                    title = json_object['Title']
                except KeyError:
                    return Response(data={'There is no movie: '+post_title}, status=status.HTTP_404_NOT_FOUND)
                if not all_movies.filter(title__iexact=title):
                    m = Movies()
                    m.title = json_object['Title']
                    m.year = json_object['Year']
                    m.rated = json_object['Rated']
                    m.released = json_object['Released']
                    m.runtime = json_object['Runtime']
                    m.genre = json_object['Genre']
                    m.director = json_object['Director']
                    m.writer = json_object['Writer']
                    m.actors = json_object['Actors']
                    m.plot = json_object['Plot']
                    m.language = json_object['Language']
                    m.country = json_object['Country']
                    m.awards = json_object['Awards']
                    m.poster = json_object['Poster']
                    m.ratings = json_object['Ratings']
                    m.metascore = json_object['Metascore']
                    m.imdb_rating = json_object['imdbRating']
                    m.imdb_votes = json_object['imdbVotes']
                    m.imdb_id = json_object['imdbID']
                    m.type = json_object['Type']
                    try :
                        m.dvd = json_object['DVD']
                    except KeyError:
                        m.dvd = 'N/A'
                    try:
                        m.boxoffice = json_object['BoxOffice']
                    except KeyError:
                        m.boxoffice='N/A'
                    try:
                        m.production = json_object['Production']
                    except KeyError:
                        m.production = 'N/A'
                    try:
                        m.website = json_object['Website']
                    except KeyError:
                        m.website = 'N/A'
                    m.response = json_object['Response']
                    m.save()
                    return Response(data={'You added movie: '+title+' to database.'}, status=status.HTTP_201_CREATED)
                else:
                    return Response(data={'Movie '+title+' already in database.'}, status=status.HTTP_400_BAD_REQUEST)







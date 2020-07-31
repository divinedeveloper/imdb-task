from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from api.models import Movie
from api.serializers import MovieSerializer

# Create your views here.


class MoviesList(generics.ListAPIView):
    """
    A simple ListAPI view for searching movies.

    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'director', 'popularity', 'imdb_score', 'genre__name']

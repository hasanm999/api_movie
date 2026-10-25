from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from movies.api.serializers import MovieSerializer
from movies.models import Movie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'description', 'year']
    search_fields = ['name', 'description', 'year']
    ordering_fields = ['year']


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.filter(is_active=True)
    permission_classes = [IsAuthenticatedOrReadOnly]



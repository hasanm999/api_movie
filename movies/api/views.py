from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from movies.api.serializers import MovieSerializer
from movies.models import Movie

class MovieListView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.filter(is_active=True)


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.filter(is_active=True)

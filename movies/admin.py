from django.contrib import admin
from movies.models import Movie

class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = ['name', 'is_active']

admin.site.register(Movie, MovieAdmin)
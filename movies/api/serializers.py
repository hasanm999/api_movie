from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # exclude = ['id']
        # read_only_fields = ['name']

    def validate_name(self, data):
        if len(data) <= 2:
            raise serializers.ValidationError('Movie name must be greater than 2')
        print(data)
        return data

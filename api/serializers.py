from rest_framework import serializers
from .models import Movie, Person

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['primary_title', 'start_year', 'title_type', 'genres']

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['primary_name', 'birth_year', 'primary_profession', 'known_for_titles']

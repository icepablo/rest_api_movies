from rest_framework import serializers
from moviesapp.models import Movies,Comments,Add

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields='__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields='__all__'
class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model=Add
        fields = '__all__'

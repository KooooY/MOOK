from rest_framework import serializers
from rest_framework import serializers
from .models import Movie, Review, Comment, Mbti, Guest

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'overview',
            'release_date',
            'tmdb_score',
            'poster_url',
            'popularity',
            'genre',
         )

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'movie',
            'title',
            'content',
            'created_at',
            'updated_at',
        )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'review',
            'content',
            'created_at',
            'updated_at',
        )

class MbtiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mbti
        fields = (
            'user',
            'genre',
        )


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = (
            'id',
            'guest',
            'owner',
            'content',
            'created_at',
            'updated_at',
        )
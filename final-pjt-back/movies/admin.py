from django.contrib import admin
from .models import Movie, Review, Genre, Comment, Mbti, Movie_like, Guest
# Register your models here.
@admin.register(Movie, Review, Genre, Comment, Mbti, Movie_like, Guest)
class MovieAdmin(admin.ModelAdmin):
    pass
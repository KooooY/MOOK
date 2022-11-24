from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    
    path('genre/<str:name>/', views.movie_genre),

    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('reviews/comments/<int:review_pk>/', views.comment_create),

    path('mbti/', views.mbti_list),
    path('mbti/<int:user_pk>', views.mbti_movies),

    path('movies/<int:movie_pk>/like/', views.movie_like),
    path('like/<int:movie_pk>/', views.like_show),

    path('search/movies', views.search),

    #profile 페이지에 방명록을 달겟어
    path('guests/', views.guest_list),
    path('guests_detail/<int:owner_pk>/<int:guest_pk>/', views.guest_detail),
    path('guests_create/<int:owner_pk>/<int:guest_pk>/', views.guest_create),
]
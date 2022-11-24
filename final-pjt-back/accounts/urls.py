from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    # path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'), #팔로잉 추가, 제거
    path('users/', views.users, name='users'),
    path('users/<int:user_pk>/', views.user, name='user'),
    # path('<int:user_pk>/follows/', views.follow, name='follow'),
    path('profile/<str:username>/', views.profile),
    
    path('follow/<int:user_pk>/', views.showfollow),          #팔로워, 팔로잉 보여주기
]

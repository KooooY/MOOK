from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    # print(request.__dict__)
    User = get_user_model()
    me = request.user
    you = User.objects.get(pk=user_pk)
    # print('memememememememem', me)
    # is_followed = 
    if me != you:
        # 내가(request.user) 그 사람의 팔로워 목록에 있다면
        # if me in you.followers.all():
        if you.followers.filter(pk=me.pk).exists():
            # 언팔로우
            you.followers.remove(me)
            
        else:
            # 팔로우
            you.followers.add(me)
            

    # followers = []
    # followings = []

    # youfollowers = you.followers.all()
    # youfollowings= you.followings.all()

    # for i in youfollowers:
    #     followers.append(i)

    # for i in youfollowings:
    #     followings.append(i)

    # # print(is_followed)
    # data = {
    #     # 'followings': you.followings.all(),
    #     # 'followers': you.followers.all(),
    #     'followings_count': len(followings),
    #     'followers_count' : len(followers),
    #     }

    return Response(200)

@api_view(['POST'])
def showfollow(request, user_pk):
    User = get_user_model()
    me = User.objects.get(pk = request.data['userId'])
    print(me)
    you = User.objects.get(pk=user_pk)
    if you.followers.filter(pk = me.pk).exists():
        follow= True
        
    else:
        follow= False
        print(False)
    
    # if you.followers.filter(pk=me).exist():
    #     pass
    # else:
    #     follow=False

    data = {
        # 'followings': you.followings.all(),
        # 'followers': you.followers.all(),
        'followings_count': you.followings.count(),
        'followers_count' : you.followers.count(),
        'follow_bull': follow
    }
    return JsonResponse(data)


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    print(user)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    # print(serializer.data)
    return Response(serializer.data)

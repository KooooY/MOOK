from django.shortcuts import render
from .models import Movie, Review, Genre, Comment, Mbti, Movie_like, Guest
from .serializers import MovieListSerializer, ReviewSerializer, CommentSerializer, MbtiSerializer, GuestSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse

from accounts.models import User
from django.contrib.auth import get_user_model

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def movie_list(request):
    movies = Movie.objects.all()
    print(movies)
    serializer = MovieListSerializer(movies, many=True)
    print(serializer)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    # print(serializer.data)
    return Response(serializer.data)

#장르 별 영화 추천
@api_view(['GET'])
def movie_genre(request, name):
    genre = Genre.objects.get(name = name)
    movies = Movie.objects.filter(genre=genre.pk)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# def mbti(request): #user 데이터와 mbti 리스트를 받았다
#     me = request.user
#     if me.mbti.filter(pk=me.pk).exist():
#         pass
#     else:
#         me.



#전체 리뷰 리스트 조회
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        User = get_user_model()
        a = User.objects.get(username=request.data['user'])
        newData = {'user':a.pk, 'movie':request.data['movie'], 'title':request.data['title'], 'content':request.data['content']}
        serializer = ReviewSerializer(data=newData)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)


#개별 리뷰 조회, 수정, 삭제
@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 

    elif request.method == 'PUT':       #여기도 data 가져오는데 user id를 가져올 수 없는가.. 일단
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True): ##raise_exeption 일단 넣어둠
            serializer.save()
            return Response(serializer.data)
    




#comment 전부 조회
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

#comment 수정,삭제,조회
@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    

#comment 생성
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    print('보내 졋냐냔냐냐냐ㅑㄴ나ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ')
    # article = Article.objects.get(pk=article_pk)
    # review = get_object_or_404(Review, pk=review_pk)

    User = get_user_model()
    a = User.objects.get(username=request.data['user'])
    newData = {'user':a.pk, 'review':request.data['review'], 'content':request.data['content']}
    
    serializer = CommentSerializer(data=newData)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


#전체 mbti 리스트 조회 및 생성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mbti_list(request):
    if request.method == 'GET':
        mbtis = Mbti.objects.all()
        serializer = MbtiSerializer(mbtis, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        mbti_dic = {
            'd': 99,
            'f': 14,
            'a': 28,
            'r': 10749,
            'c': 35,
            't': 53,
            'h': 27,
            'n': 16,
        }
        print(request.data)
        print(request.user)
        print(Mbti.objects.filter(pk=request.user.pk))
        if len(Mbti.objects.filter(user=request.user))!=0:
            pass
        else:
            mbtis = list(request.data['mbtiType'])
            print(mbtis)
            for i in mbtis:
                genre = Genre.objects.get(pk=mbti_dic[i])
                Mbti.objects.create(user=request.user, genre= genre)
            # for i in range(len(request.data['mbti'])):
            #     request.user.mbti.add(request.data['mbti'][i])
        
        return Response(status=status.HTTP_201_CREATED)



#mbti를 통해 영화 리스트 보내기

@api_view(['GET'])
def mbti_movies(request, user_pk):
    m_genres = Mbti.objects.filter(user=user_pk)
    print(m_genres)
    genre_list = [] #2번 mbti 장르 객체를 담았다.. 4개
    for o in m_genres:
        genre_list.append(o.genre.pk)
    
    

    movies = Movie.objects.filter(genre__in =genre_list)
    # for genre in genre_list:
    #     movies.append(Movie.objects.filter(genre=genre.pk))

    # print(movies)

    # # movies = Movie.objects.filter(genre=genre.pk)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

    # print(genre_list)


#영화 좋아요 디비에 저장
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    me = request.user
    movie = Movie.objects.get(pk=movie_pk)
    # print(me.pk)
    # print(len(Movie_like.objects.filter(movie=19995, user=2)))
    if len(Movie_like.objects.filter(movie=movie_pk, user=me.pk))==0:
        Movie_like.objects.create(movie=movie, user=me)

    else:
        Movie_like.objects.filter(movie=movie_pk, user=me.pk).delete()

    return Response('200')

#영화상세페이지에서 좋아요 개수 보여주기
@api_view(['POST'])
def like_show(request, movie_pk):
    likes = Movie_like.objects.filter(movie=movie_pk)
    like_people = []
    for like in likes:
        like_people.append(like.user_id)
    user = request.data['userId']
    print(request.__dict__)
    print(like_people)
    print(user)
    like_bool = False
    if user in like_people:
        like_bool = True

    data = {
        'likes_count': len(likes),
        'like_bool' : like_bool,
        
    }
    return JsonResponse(data)

@api_view
def search(request):
    movies = Movie.objects.all()
    movie_list = []
    for movie in movies:
        if request.data['string'] in movie.title:
            movie_list.append(movie.pk)


##방명록을 달아보겠습니다다다닫다ㅏ닫다다다

#guest 전부 조회
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def guest_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        guests = get_list_or_404(Guest)
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

#guest comment 수정,삭제,조회
@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def guest_detail(request, owner_pk, guest_pk):
    comment = Guest.objects.get(pk=request.data['a'])
    # comment = get_object_or_404(Guest, owner = owner, guest = guest)
    print('ssssss',comment)
    if request.method == 'GET':
        serializer = GuestSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = GuestSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    

#guest comment 생성
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def guest_create(request, owner_pk, guest_pk):
    # print('보내 졋냐냔냐냐냐ㅑㄴ나ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ')
    # article = Article.objects.get(pk=article_pk)
    # review = get_object_or_404(Review, pk=review_pk)

    # User = get_user_model()
    # a = User.objects.get(username=request.data['user'])
    # newData = {'user':a.pk, 'review':request.data['review'], 'content':request.data['content']}
    newData = {'guest':guest_pk, 'owner':owner_pk, 'content':request.data['content']}
    
    serializer = GuestSerializer(data=newData)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
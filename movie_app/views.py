from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status


@api_view(['GET'])
def director_list_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={
            "message": f"Режиссёр не найден"
        }, status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_list_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={
            "message": f"Фильм не найден"
        }, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieDetailSerializer(movie)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={
            "message": f"Отзыв не найден"
        }, status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewDetailSerializer(review)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

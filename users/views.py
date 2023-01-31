from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from users.serializers import UserCreateSerializer, UserValidateSerializer


@api_view(['POST'])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def authorization(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=status.HTTP_403_FORBIDDEN)

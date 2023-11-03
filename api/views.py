from django.shortcuts import render

from django.contrib.auth import login
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from api.models import Game, Slide, Tourney
from api.serializers import GameSerializer, SlideSerializer, TourneySerializer
# from rest_framework import permissions
# from rest_framework.authtoken.serializers import AuthTokenSerializer


# Create your views here.

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def slideList(request):
    if(request.method == 'GET'):
        slides = Slide.objects.all()
        serializer = SlideSerializer(slides, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def gameList(request):
    if(request.method == 'GET'):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def gameDetails(request, pk):
    if(request.method == 'GET'):
        games = Game.objects.filter(pk=pk)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def tourneyList(request):
    if(request.method == 'GET'):
        tourney = Tourney.objects.all()
        serializer = TourneySerializer(tourney, many=True)
        return Response(serializer.data)
    elif(request.method == 'POST'):
        serializer = TourneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def tourneyDetails(request, pk):
    if(request.method == 'GET'):
        tourney = Tourney.objects.filter(pk=pk)
        serializer = TourneySerializer(tourney, many=True)
        return Response(serializer.data)

# class LoginAPI(KnoxLoginView):
#     permission_classes = ([AllowAny])
#     def post(self, request, format=None):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return super(LoginAPI, self).post(request, format=None)

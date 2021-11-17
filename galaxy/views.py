from django.shortcuts import render
from rest_framework import generics
from .serializers import CharacterListSerializer, FilmListSerializer
from .models import Character, Film


class CharacterListAPIView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer


class FilmListAPIView(generics.ListAPIView):
    queryset= Film.objects.all()
    serializer_class = FilmListSerializer




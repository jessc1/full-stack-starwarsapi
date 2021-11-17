from django.shortcuts import render
from rest_framework import generics
from .serializers import CharacterListSerializer, CharacterDetailSerializer, FilmListSerializer
from .models import Character, Film


class CharacterListAPIView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer

class CharacterRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the character's detail in the API 
    """
    lookup_field = "id"
    queryset = Character.objects.all()
    serializer_class = CharacterDetailSerializer
    


class FilmListAPIView(generics.ListAPIView):
    queryset= Film.objects.all()
    serializer_class = FilmListSerializer




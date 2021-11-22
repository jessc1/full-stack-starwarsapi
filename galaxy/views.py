#from django.shortcuts import render
from rest_framework import generics
from .serializers import CharacterListSerializer, CharacterDetailSerializer, \
     FilmListSerializer, FilmDetailSerializer, PlanetListSerializer, PlanetDetailSerializer, \
     StarshipListSerializer, StarshipDetailSerializer, VehicleListSerializer, VehicleDetailSerializer, \
     SpecieListSerializer, SpecieDetailSerializer
     
from .models import Character, Film, Planet, Transport, Starships, Vehicles, Species


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

class FilmRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the movie's detail in the API 
    """
    lookup_field = "id"
    queryset = Film.objects.all()
    serializer_class = FilmDetailSerializer

class PlanetListAPIView(generics.ListAPIView):
    """
    Return the planet's list 
    """    
    queryset = Planet.objects.all()
    serializer_class = PlanetListSerializer


class PlanetRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the planet's detail in the API 
    """
    lookup_field = "id"
    queryset = Planet.objects.all()
    serializer_class = PlanetDetailSerializer


class StarshipListAPIView(generics.ListAPIView):
    """
    Return the starship's list 
    """
    queryset = Starships.objects.all()
    serializer_class = StarshipListSerializer


class StarshipRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the starship's detail in the API 
    """
    lookup_field = "id"
    queryset = Starships.objects.all()
    serializer_class = StarshipDetailSerializer    
    
class VehicleListAPIView(generics.ListAPIView):
    """
    Return the vehicle's list in the API 
    """
    
    queryset = Vehicles.objects.all()
    serializer_class = VehicleListSerializer


class VehicleRetrieveAPIView(generics.RetrieveAPIView):
    """
    Return the vehicle's list in the API 
    """
    lookup_field = "id"
    queryset = Vehicles.objects.all()
    serializer_class = VehicleDetailSerializer


class SpecieListAPIView(generics.ListAPIView):
    """
    Return the vehicle's list in the API 
    """
    
    queryset = Species.objects.all()
    serializer_class = SpecieListSerializer

class SpecieRetrieveAPIView(generics.ListAPIView):
    """
    Return the species's detail in the API 
    """
    lookup_field = "id"
    queryset = Species.objects.all()
    serializer_class = SpecieDetailSerializer    
  


    




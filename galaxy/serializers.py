from rest_framework import serializers
from galaxy.models import Character, Film, Planet, Starships, Vehicles, Species

class CharacterListSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Character
        fields = '__all__'

class CharacterDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Character
        fields = '__all__'    

class FilmListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Film
        fields = '__all__'

class FilmDetailSerializer(serializers.ModelSerializer):
    class Meta:                  
        model = Film
        fields = '__all__'

class PlanetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class PlanetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Planet
        fields = '__all__'

class StarshipListSerializer(serializers.ModelSerializer):
    class Meta:           
        model = Starships
        fields = '__all__'

class StarshipDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Starships
        fields = '__all__'

class VehicleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = '__all__'

class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = '__all__'

class SpecieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'

class SpecieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'    
            
            
    
        

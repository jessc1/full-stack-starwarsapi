from rest_framework import serializers
from galaxy.models import Character, Film

class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class FilmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'
        

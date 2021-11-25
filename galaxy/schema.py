import graphene
from graphene_django import DjangoObjectType, DjangoListField
from galaxy.models import Character, Film, Planet, Species, Vehicles, Starships

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = "__all__"



class FilmType(DjangoObjectType):
    class Meta:
        model = Film
        fields = "__all__"


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet
        fields = "__all__"

class SpeciesType(DjangoObjectType):
    class Meta:
        model = Species
        fields = "__all__"
    
class VehiclesType(DjangoObjectType):
    class Meta:
        model = Vehicles
        fields = "__all__"

class StarshipsType(DjangoObjectType):
    class Meta:
        model = Starships
        fields = "__all__"

    
class Query(graphene.ObjectType):
    all_characters = graphene.List(CharacterType)
    character = graphene.Field(CharacterType, id=graphene.Int())
    all_films = graphene.List(FilmType)
    film = graphene.Field(FilmType, id=graphene.Int())
    all_planets = graphene.List(PlanetType)
    planet = graphene.Field(PlanetType, id=graphene.Int())
    all_species = graphene.List(SpeciesType)
    specie = graphene.Field(SpeciesType, id=graphene.Int())
    all_vehicles = graphene.List(VehiclesType)
    vehicle = graphene.Field(VehiclesType, id=graphene.Int())
    all_starships = graphene.List(StarshipsType)
    starship = graphene.Field(StarshipsType, id=graphene.Int())
    

    def resolve_all_characters(self, info, **kwargs):
        return Character.objects.all()
    

    def resolve_character(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Character.objects.get(pk=id)

        return None

    def resolve_all_films(self, info, **kwargs):
        return Film.objects.all()

    def resolve_film(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Film.objects.get(pk=id)

        return None

    def resolve_all_planets(self, info, **kwargs):
        return Planet.objects.all()

    def resolve_planet(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Planet.objects.get(pk=id)

        return None
    
    def resolve_all_species(self, info, **kwargs):
        return Species.objects.all()
    
    def resolve_specie(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Species.objects.get(pk=id)

        return None

    def resolve_all_vehicles(self, info, **kwargs):
        return Vehicles.objects.all()

    def resolve_vehicle(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Vehicles.objects.get(pk=id)

        return None

    def resolve_all_starships(self, info, **kwargs):
        return Starships.objects.all()

    def resolve_starship(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Starships.objects.get(pk=id)

        return None
    

schema = graphene.Schema(query=Query)

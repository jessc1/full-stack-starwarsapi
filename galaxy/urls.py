from django.urls import path
from graphene_django.views import GraphQLView 
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('starwars/character/list',views.CharacterListAPIView.as_view(), name='characters'),
    path('starwars/character/<int:id>', views.CharacterRetrieveAPIView.as_view(), name='character_detail'),
    path('starwars/planets/', views.PlanetListAPIView.as_view(), name='planets'),
    path('starwars/planet/<int:id>', views.PlanetRetrieveAPIView.as_view(), name='planet_detail'),
    path('starwars/starships', views.StarshipListAPIView.as_view(), name='starships'),
    path('starwars/starship/<int:id>', views.StarshipRetrieveAPIView.as_view(), name='starship_detail'),
    path('starwars/vehicles/', views.VehicleListAPIView.as_view(), name='vehicles'),
    path('starwars/vehicle/<int:id>', views.VehicleRetrieveAPIView.as_view(), name='vehicles_detail'),
    path('starwars/species', views.SpecieListAPIView.as_view(), name='species'),
    path('starwars/species/<int:id>', views.SpecieRetrieveAPIView.as_view(), name='species_detail'),
    path('starwars/film/list',views.FilmListAPIView.as_view(), name='films'),
    path('starwars/film/<int:id>', views.FilmRetrieveAPIView.as_view(), name='film_detail'),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
    
    

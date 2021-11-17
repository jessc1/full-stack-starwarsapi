from django.urls import path
from . import views

urlpatterns = [
    path('starwars/character/list',views.CharacterListAPIView.as_view(), name='characters'),
    path('starwars/film/list',views.FilmListAPIView.as_view(), name='films'),
    
    ]

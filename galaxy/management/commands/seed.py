import requests
import json
from django.core.management.base import BaseCommand
from galaxy.models import Character, Film, Planet, Starships, Species, Vehicles




#def get_next():
  
  #total_results = []
  #url = 'https://swapi.dev/api/people'
  #response=requests.get(url)
  #character = response.json()
  
  #total_results = total_results + character['results']
  #while character['next'] is not None:
    #print("Next page found, downloading", character['next'])
    #response = requests.get(character['next'])
    #character = response.json()
    
    
    #total_results = total_results + character['results']
  
   # print(len(total_results))


def get_people(link):
  response=requests.get(link)
  
  character = response.json()
  
  
  api = response.json()
  total = []
  
  for i in api['results']:
    
   character = Character(
      name = i['name'],
      height= i['height'],
      mass = i['mass'],
      hair_color = i['hair_color'],
      skin_color = i['skin_color'],
      eye_color = i['eye_color'],
      birth_year = i['birth_year'],
      gender=i['gender'],
      homeworld = i['homeworld'],
      film = i['films'],
      species=i['species'],
      vehicles=i['vehicles'],
      starships=i['starships'],
      created = i['created'],
      edited = i['edited'],
      url = i['url'],    
           
   )
   character.save()
   
  total = total + api['results']
 
  
  while api['next']is not None:

    
    print(api['next'])
    response = requests.get(api['next'])
    api = response.json()
    for i in api['results']:
        
     character = Character(
       
       name = i['name'],
       height= i['height'],
       mass = i['mass'],
       hair_color = i['hair_color'],
       skin_color = i['skin_color'],
       eye_color = i['eye_color'],
       birth_year = i['birth_year'],
       gender=i['gender'],
       homeworld = i['homeworld'],
       film = i['films'],
       species=i['species'],
       vehicles=i['vehicles'],
       starships=i['starships'],
       created = i['created'],
       edited = i['edited'],
       url = i['url'],    
           
     )
     character.save()
    
     total = total + api['results']
  return total
    #return total
    #return next_page
    #for page in next_page:
     # yield page
    #response = requests.get(api['next'])
    
    #api = json.loads(response.text)
    #total = total + api['results']
    #print(total)
    #print(api['next'])
  #return character
    
    #next_page = get_people(api['next'])
    #print(next_page)
    #3for p in next_page:
      #print(p)
      #yield p
  #return Character


    #while api[']
  
      
 


#def get_planet():
 # url = 'https://swapi.dev/api/planets'
  #r = requests.get(url, headers={'Content-Type':      
   # 'application/json'})
  #planet = r.json()
  #api = json.loads(r.text)
  #for i in api['results']:
    
   # planet = Planet(
      
    #  name = i['name'],
     # rotation_period= i['rotation_period'],
      #orbital_period = i['orbital_period'],
      #diameter = i['diameter'],
      #climate = i['climate'],
      #gravity = i['gravity'],
      
      #terrain = i['terrain'],
      #surface_water = i['surface_water'],
      #population = i['population'],      
      #created = i['created'],
      #edited = i['edited'],
      #url = i['url'],    
           
    #)
    #planet.save()

  


  
 # while api['next']:
  #  print(api['next'])
   # r = requests.get(api['next'])
    
    
   
  
    #next_page = get_planet(api['next'])
    #print(next_page)
    #for p in next_page:
     # yield p
      #print(p)


      

  

#def get_starships(link):
 # response=requests.get(link)
  
  #starships = response.json()
  
  #api = json.loads(response.text)
  #for i in api['results']:
   # starships = Starships(
    #  hyperdrive = i['hyperdrive'],
     # MGLT= i['MGLT'],
      #starship_class = i['starship_class'],
      #pilots = i['pilots'],
        
           
    #)
    #starships.save()
  #while api['next'] is not None:
    #print(api['next'])
    #next_page = get_starships(api['next'])
    #print(next_page)
    #for p in next_page:
     # yield p
      #print(p)


#def get_vehicle(link):
 # response=requests.get(link)
  
  #vehicle = response.json()
  
  #api = json.loads(response.text)
  #for i in api['results']:
    #vehicle = Vehicles(
     # vehicle_class = i['vehicle_class'],
     # pilots= i['pilots'],
      
    #)
    #vehicle.save()
  #while api['next'] is not None:
   # print(api['next'])
    #next_page = get_vehicle(api['next'])
    #print(next_page)
    #for p in next_page:
     # yield p
      #print(p)



  
  #film = response.json()
  
 # api = json.loads(response.text)
#  for i in api['results']:
    #film = Film(
     # title = i['title'],
     # episode_id =i['episode_id'],
     # opening_craw = i['opening_craw'],
     # director = i['director'],
     # producer = i['producter'],
     # release_date = i['release_date'],
      #characters = i['characters'],
      #planets = i['planets'],
      #starships = i['staships'],
      #vehicles = i['vehicles'],
      #species = i['species'],
      #created = i['created'],
      #edited = i['edited'],
      #url = i['url'],
     # 
    #)
   # film.save()
  #w3ile api['next'] is not None:
    #print(api['next'])
    #next_page = get_film(api['next'])
    #print(next_page)
    #for p in next_page:
      #yield p
      #print(p)
    
  


    
  
  
  #api = json.loads(response.content)
  #for i in api['results']:
     # character = Character(
      #  name = i['name']
     # )
      #character.save()

  
  
  #while api['next'] is not None:
   # response = requests.get(character['next'])
   # character = response.json()
   # total_results = total_results + character['results']


   
    
  
    
  


    
        
       
       
        
    
    
      
  


#def get_film():
 # response=requests.get( 'https://swapi.dev/api/films')
  #film=response.json()
  #api = json.loads(response.text)
  #for i in api['results']:
   # film = Film(
    #  title = i["title"],
     # episode_id= i["episode_id"],
      #director= i["director"],
      #producer= i["producer"],
      #release_date=i["release_date"],               
      #created=i["created"],                   
      #edited =i["edited"],
    #  url = i["url"]
    #)
    #film.save()
  #Return Film
      
  
    




class Command(BaseCommand):
  def handle(self, *args, **options):
    print(get_people('https://swapi.dev/api/people'))
    #print(seed_planet())
    #print(get_people())
    
    #print(get_starships('https://swapi.dev/api/starships'))
    #print(get_vehicle('https://swapi.dev/api/vehicles'))
    #print(get_species('https://swapi.dev/api/species'))
    #print(get_film('https://swapi.dev/api/films'))
    
    #get_film()
    # clear_data()
    print("completed")

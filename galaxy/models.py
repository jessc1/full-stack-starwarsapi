from django.db import models




class Planet(models.Model):
    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=50)
    orbital_period = models.CharField(max_length=50)
    diameter = models.CharField(max_length=50)
    climate = models.CharField(max_length=50)
    gravity = models.CharField(max_length=50)
    terrain = models.CharField(max_length=50)
    surface_water = models.CharField(max_length=50)
    population = models.CharField(max_length=50)
    residents = models.CharField(max_length=50)
    films = models.CharField(max_length=100)
    
    created=models.DateTimeField \
                   (auto_now_add=True, \
                    help_text= \
                    "The date and time the movie'data was created.")
    edited = models.DateTimeField \
                   (null=True, \
                    help_text= \
                    "The date and time the movie was edited.")
    url = models.URLField \
              (help_text = "The url's movie .")
    def __str__(self):
        return self.name


    
class Character(models.Model):
    
    name=models.CharField(max_length=100)
    height = models.CharField(max_length=10, blank=True)
    mass = models.CharField(max_length=10, blank=True)
    hair_color = models.CharField(max_length=20, blank=True)
    skin_color = models.CharField(max_length=20, blank=True)
    eye_color = models.CharField(max_length=20, blank=True)
    birth_year = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    homeworld =  models.CharField(max_length=30, blank=True)   
    film =  models.CharField(max_length=30, blank=True)
    species =  models.CharField(max_length=30, blank=True)
    vehicles = models.CharField(max_length=30, blank=True)
    starships = models.CharField(max_length=30, blank=True)  
    
    created=models.DateTimeField \
                   (auto_now_add=True, \
                    help_text= \
                    "The date and time the movie'data was created.")
    edited = models.DateTimeField \
                   (null=True, \
                    help_text= \
                    "The date and time the movie was edited.")
    url = models.URLField \
              (help_text = "The url's movie .")
    def __str__(self):
        return self.name

class Transport(models.Model):
    
    name = models.CharField(max_length=50)
    model =models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    cost_in_credits= models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    max_atmosphering_speed = models.CharField(max_length=50)
    crew = models.CharField(max_length=50)
    passengers = models.CharField(max_length=50)
    cargo_capacity = models.CharField(max_length=50)
    consumables = models.CharField(max_length=50)
    pilots = models.CharField(max_length=50)
    films =  models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

    
class Starships(Transport):
    hyperdrive_rating = models.CharField(max_length=50)
    MGLT = models.CharField(max_length=50)
    starship_class = models.CharField(max_length=50)
    

class Vehicles(Transport):
    vehicle_class = models.CharField(max_length=50)
    
    

class Species(models.Model):
    name = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    average_height =models.CharField(max_length=50)
    skin_color = models.CharField(max_length=50)
    hair_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    average_lifespan = models.CharField(max_length=50)    
    language = models.CharField(max_length=50)
    people = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Film(models.Model):
    title = models.CharField(max_length=200)
    episode_id=models.IntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director=models.CharField(max_length=100)
    producer=models.CharField(max_length=100)
    release_date=models.DateTimeField \
                   (null=True, \
                    help_text= \
                    "The date and time the movie was released.")
    characters = models.CharField(max_length=50)
    planets = models.CharField(max_length=50)
    starships = models.CharField(max_length=50)
    vehicles = models.CharField(max_length=50)
    species = models.CharField(max_length=50)        
    created=models.DateTimeField \
                   (auto_now_add=True, \
                    help_text= \
                    "The date and time the movie'data was created.")
    edited = models.DateTimeField \
                   (null=True, \
                    help_text= \
                    "The date and time the movie was edited.")
    url = models.URLField \
              (help_text = "The url's movie .")

    def __str__(self):
        return self.title



    
    

    def __str__(self):
        return self.name    

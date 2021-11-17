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
    #residents = models.ManyToManyField(
     #   Character,
      #  related_name="pessoa",
       # blank=True
    #)
    #residents = models.ForeignKey \
     #           (Character, related_name="character", on_delete=models.CASCADE)
    #residents= models.ForeignKey(Character, related_name="characters", on_delete=models.CASCADE)
    #films = models.ForeignKey(Film, related_name="films")
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
    #films = models.ManyToManyField(
     #   Film,
      #  related_name ="film",
       # blank=True
    #)
    film =  models.CharField(max_length=30, blank=True)
    species =  models.CharField(max_length=30, blank=True)
    vehicles = models.CharField(max_length=30, blank=True)
    starships = models.CharField(max_length=30, blank=True)
    
    #species = models.ManyToManyField(
     #   Species,
      #  related_name ="species",
       # blank=True
    #)
    #vehicles = models.ManyToManyField(
     #   Vehicles,
      #  related_name ="vehicles",
       # blank=True
    #)
    #species = films = models.ManyToManyField \
     #              ('Species')
    #vehicle = models.ManyToManyField \
     #              ('Vehicles')
    #starships = models.ManyToManyField(
     #   Starships,
      #  related_name ="starships",
       # blank=True
        #)
    #starship = models.ManyToManyField \
     #              ('Starships')
    #homeworld = models.ForeignKey(Planet, related_name ="residents",on_delete=models.CASCADE)
    #films = models.ForeignKey(Film, related_name="films")
    #species = models.ForeignKey(Film, related_name="species")
    #vehicles = models.ForeignKey(Film, related_name="vehicles")
    #starships = models.ForeignKey(Film, related_name="starships")
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

    def __str__(self):
        return self.name

    
class Starships(Transport):
    hyperdrive_hating = models.CharField(max_length=50)
    MGLT = models.CharField(max_length=50)
    starship_class = models.CharField(max_length=50)
    #pilots = models.ManyToManyField(
     #   Character,
      #  related_name ="starships",
       # blank=True
        #)

class Vehicles(models.Model):
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
    #homeworld = models.ForeignKey(Planet, blank=True, null=True, on_delete=models.CASCADE)
    #language = models.CharField(max_length=50)
    #people = models.ManyToManyField(Character, related_name="species")

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
    #characters = models.ManyToManyField(
     #   Character,
      #  related_name="characters",
       # blank=True
    #)
    #planets = models.ManyToManyField(
     #   Planet,
      #  related_name="planets",
       # blank=True
        #)
    #starships = models.ManyToManyField(
        #Starships,
        #related_name="starships",
        
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

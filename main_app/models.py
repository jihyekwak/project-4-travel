from django.db import models
from django.contrib.postgres.fields import ArrayField
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    
        profile_image = models.ImageField(upload_to = "profile_images/", blank=True, null=True)

CONTINENT_CHOICES = {
    ("Africa", "Africa"),
    ("Antarctica", "Antarctica"),
    ("Asia", "Asia"),
    ("Europe", "Europe"),
    ("North America", "North America"),
    ("Oceania", "Oceania"),
    ("Sourth America", "South America"),
}

class Destination(models.Model):

    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    continent = models.CharField(max_length= 50, choices= CONTINENT_CHOICES, null=True)
    image = models.ImageField(upload_to = "destination_images/", blank=True)
    description = models.TextField()
    things_to_do = ArrayField(models.CharField(max_length = 250), blank = True)

    def __str__(self):
        return self.city

    class Meta:
        ordering = ['country']

class Tag(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Travel(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "travel_images/", blank=True)
    destinations = models.ManyToManyField(Destination, blank=True)
    departure_date = models.DateField(auto_now = False, auto_now_add = False)
    return_date = models.DateField(auto_now = False, auto_now_add = False)
    budget = models.IntegerField()
    travelers = models.ManyToManyField(CustomUser)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['departure_date']

class Itinerary(models.Model):

    day = models.IntegerField()
    date = models.DateField(auto_now = False, auto_now_add = False)
    destination = models.ForeignKey(Destination, related_name='itineraries', on_delete = models.CASCADE, null=True, blank=True)
    transportation = models.CharField(max_length=250)
    accomodation = models.CharField(max_length=250)
    things_to_do = ArrayField(models.CharField(max_length=250))
    meals = ArrayField(models.CharField(max_length=50))
    daily_budget = models.IntegerField(default = 0)
    travel = models.ForeignKey(Travel, related_name='itineraries', on_delete = models.CASCADE)

    def __str__(self):
        return 'Day' + str(self.day) + '_'+str(self.travel)
    
    class Meta:
        ordering = ['date']

CATEGORY_CHOICES = {
    ("To Do List", "To Do List"), 
    ("Check List", "Check List"),
    ("Packing List", "Packing List"), 
}

PRIORITY_CHOICES = {
    ("High", "High"), 
    ("Medium", "Medium"), 
    ("Low", "Low"), 
    ("None", "None")
}

class List(models.Model):

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    item = models.CharField(max_length=250)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, blank=True)
    is_completed = models.BooleanField(default = False)
    due_date = models.DateField(auto_now = False, auto_now_add = False, blank=True, null=True)
    travel = models.ForeignKey(Travel, related_name='lists', on_delete=models.CASCADE)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ['category', 'is_completed']

class Comment(models.Model):

    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    travel = models.ForeignKey(Travel, related_name='comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return 'Comment' + str(self.pk) + '_'+ str(self.travel)
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Travel(models.Model):

    title = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    departure_date = models.DateField(auto_now = False, auto_now_add = False)
    return_date = models.DateField(auto_now = False, auto_now_add = False)
    budget = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['departure_date']

class Itinerary(models.Model):

    day = models.IntegerField()
    date = models.DateField(auto_now = False, auto_now_add = False)
    transportation = models.CharField(max_length=250)
    accomodation = models.CharField(max_length=250)
    things_to_do = ArrayField(models.CharField(max_length=250))
    meals = ArrayField(models.CharField(max_length=50))
    daily_budget = models.IntegerField(default = 0)
    travel = models.ForeignKey(Travel, related_name='itineraries', on_delete = models.CASCADE)

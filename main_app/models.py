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
    transportation = models.CharField(max_length=250, blank = True)
    accomodation = models.CharField(max_length=250, blank = True)
    things_todo = ArrayField(models.CharField(max_length=250), blank = True)
    meals = ArrayField(models.CharField(max_length=50), blank = True)
    daily_budget = models.IntegerField(blank = True)
    travel = models.ForeignKey(Travel, related_name='itineraries', on_delete = models.CASCADE)

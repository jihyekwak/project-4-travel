from django.db import models

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
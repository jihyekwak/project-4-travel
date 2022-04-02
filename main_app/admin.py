from django.contrib import admin
from .models import Travel, Itinerary, Destination

# Register your models here.
admin.site.register(Travel)
admin.site.register(Itinerary)
admin.site.register(Destination)
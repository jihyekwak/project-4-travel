from django.contrib import admin
from .models import Travel, Itinerary, Destination, Comment

# Register your models here.
admin.site.register(Travel)
admin.site.register(Itinerary)
admin.site.register(Destination)
admin.site.register(Comment)
from django.contrib import admin
from .models import Travel, Itinerary, Destination, Comment, CustomUser, Tag, List
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets, 
        (
            'Profile',
            {
                'fields': (
                    'profile_image',
                )
            }
        )
    )
    
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Travel)
admin.site.register(Itinerary)
admin.site.register(Destination)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(List)
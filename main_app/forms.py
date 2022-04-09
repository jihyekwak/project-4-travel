from dataclasses import field
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Itinerary, Comment, CustomUser, Travel, Tag

class ItineraryForm(forms.ModelForm):

    class Meta:
        model = Itinerary
        fields = '__all__'

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text']

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ['username']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email',  'profile_image']
        
class TravelForm(forms.ModelForm):

    tags = forms.CharField(max_length = 100)

    class Meta:
        model = Travel
        fields = ['destinations', 'title', 'image', 'departure_date', 'return_date', 'budget', 'travelers']

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'
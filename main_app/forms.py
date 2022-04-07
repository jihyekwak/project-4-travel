from dataclasses import field
from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Itinerary, Comment, CustomUser

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
        
        
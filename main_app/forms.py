from dataclasses import field
from django import forms
from .models import Itinerary, Comment

class ItineraryForm(forms.ModelForm):

    class Meta:
        model = Itinerary
        fields = '__all__'

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['text']
        
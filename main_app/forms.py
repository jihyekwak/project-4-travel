from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Itinerary, Comment, CustomUser, Travel, Tag, List

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
        fields = ['username', 'first_name', 'last_name', 'email',  'profile_image', 'travel_bucket_list']

class DateInput(forms.DateInput):
    input_type = 'date'

class TravelForm(forms.ModelForm):

    departure_date = forms.DateField(widget = DateInput)
    return_date = forms.DateField(widget = DateInput)
    tags = forms.CharField(max_length = 100)

    class Meta:
        model = Travel
        fields = ['destinations', 'title', 'image', 'departure_date' ,'return_date', 'budget', 'travelers']

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = '__all__'

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ['category', 'item', 'priority', 'due_date']
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Travel, Itinerary, Destination, Comment
from .forms import CustomUserCreationForm, CustomUserChangeForm, ItineraryForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model


# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinations'] = Destination.objects.order_by('?')[:4]
        context['travels'] = Travel.objects.order_by('?')[:4]
        return context

class Travel_List(TemplateView):
    template_name = 'travel_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context['travels'] = Travel.objects.filter(title__icontains=title)
            context['header'] = f"Searching for {title}"
        else:
            context['travels'] = Travel.objects.all()
            context['header'] = "All Travels"
        return context

@method_decorator(login_required, name='dispatch')
class Travel_Create(CreateView):
    model = Travel
    fields = ['destinations', 'title', 'image', 'departure_date', 'return_date', 'budget', 'travelers']
    template_name = 'travel_create.html'
    success_url = '/travels/'


# class Travel_Detail(DetailView):
#     model = Travel
#     template_name = 'travel_detail.html'

def travel_detail(request, pk):
    travel = Travel.objects.get(pk = pk)
    form = CommentForm(request.POST or None)
    form.instance.travel = travel
    if request.user.is_authenticated:
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/travels/"+str(pk))
    return render(request, 'travel_detail.html', {'travel': travel, 'form':form})

@method_decorator(login_required, name='dispatch')
class Travel_Update(UpdateView):
    model = Travel
    fields = '__all__'
    template_name = 'travel_update.html'
    
    def get_success_url(self):
        return reverse('travel_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class Travel_Delete(DeleteView):
    model = Travel
    template_name = 'travel_delete_confirmation.html'
    success_url = '/travels/'

@method_decorator(login_required, name='dispatch')
class Itinerary_Create(CreateView):
    model = Itinerary
    fields = '__all__'
    template_name = 'itinerary_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        travel = self.kwargs.get("pk")
        context['travel'] = Travel.objects.get(pk=travel)
        return context

    def get_initial(self):
        return {"travel": self.kwargs.get("pk")}

    def get_success_url(self):
        return reverse('travel_detail', kwargs={'pk': self.object.travel.id})
    
    def from_valid(self, form):
        self.object = form.save(commit = False)
        self.object.travel = self.request.travel
        self.object.save()

@login_required
def itinerary_update(request, pk, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    travel = Travel.objects.get(pk=pk)
    form = ItineraryForm(request.POST or None, instance = itinerary)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/travels/"+str(pk))
    return render(request, 'itinerary_update.html', {'itineray':itinerary, 'form':form, 'travel':travel})

@login_required
def itinerary_delete(request, pk, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if request.method == "POST":
        itinerary.delete()
        return HttpResponseRedirect("/travels/"+str(pk))
    return render(request, "itinerary_delete_confirmation.html", {'itinerary':itinerary})

# def destination_list(request):
#     destinations = Destination.objects.all()
#     return render(request, 'destination_list.html', {'destinations': destinations})

class Destination_List(TemplateView):
    template_name = 'destination_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        city = self.request.GET.get("city")
        if city != None:
            context['destinations'] = Destination.objects.filter(city__icontains=city)
            context['header'] = f"Searching for {city}"
        else:
            context['destinations'] = Destination.objects.all()
            context['header'] = "All Destination"
        return context

@method_decorator(login_required, name='dispatch')
class Destination_Create(CreateView):
    model = Destination
    fields = '__all__'
    template_name = 'destination_create.html'
    success_url = "/destinations/"

class Destination_Detail(DetailView):
    model = Destination
    template_name = 'destination_detail.html'

@method_decorator(login_required, name='dispatch')
class Destination_Update(UpdateView):
    model = Destination
    fields = '__all__'
    template_name = 'destination_update.html'
    
    def get_success_url(self):
        return reverse('destination_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class Destination_Delete(DeleteView):
    model = Destination
    template_name = 'destination_delete_confirmation.html'
    success_url = "/destinations/"

@login_required
def comment_update_delete(request, pk, comment_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(request.POST or None, instance = comment)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/travels/"+str(pk))
    if request.method == "POST":
        comment.delete()
        return HttpResponseRedirect("/travels/"+str(pk))
    return render(request, 'comment_update.html', {'comment':comment, 'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    return render(request, 'login.html', {'form': form})
            else:
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Hi', user.username)
            return HttpResponseRedirect('/user/' + str(user))
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form':form})

@login_required
def profile(request, username):
    user = get_user_model().objects.get(username = username)
    return render(request, 'profile.html', {'user':user})

@method_decorator(login_required, name='dispatch')
class Profile_Update(UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'profile_update.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'username': self.object.username})

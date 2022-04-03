from dataclasses import field
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Travel, Itinerary, Destination, Comment
from .forms import ItineraryForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

class Travel_Create(CreateView):
    model = Travel
    fields = '__all__'
    template_name = 'travel_create.html'
    success_url = '/travels/'

# class Travel_Detail(DetailView):
#     model = Travel
#     template_name = 'travel_detail.html'

def travel_detail(request, pk):
    travel = Travel.objects.get(pk = pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/travels/"+str(pk))
    return render(request, 'travel_detail.html', {'travel': travel, 'form':form})

class Travel_Update(UpdateView):
    model = Travel
    fields = '__all__'
    template_name = 'travel_update.html'
    
    def get_success_url(self):
        return reverse('travel_detail', kwargs={'pk': self.object.pk})

class Travel_Delete(DeleteView):
    model = Travel
    template_name = 'travel_delete_confirmation.html'
    success_url = '/travels/'

class Itinerary_Create(CreateView):
    model = Itinerary
    fields = '__all__'
    template_name = 'itinerary_create.html'

    def get_success_url(self):
        return reverse('travel_detail', kwargs={'pk': self.object.travel.id})
    
    def from_valid(self, form):
        self.object = form.save(commit = False)
        self.object.travel = self.request.travel
        self.object.save()

def itinerary_update(request, pk, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    form = ItineraryForm(request.POST or None, instance = itinerary)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/travels/"+str(pk))
    return render(request, 'itinerary_update.html', {'itineray':itinerary, 'form':form})

def itinerary_delete(request, pk, itinerary_id):
    itinerary = Itinerary.objects.get(id=itinerary_id)
    if request.method == "POST":
        itinerary.delete()
        return HttpResponseRedirect("/travels/"+str(pk))
    return render(request, "itinerary_delete_confirmation.html", {'itinerary':itinerary})

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destination_list.html', {'destinations': destinations})

class Destination_Create(CreateView):
    model = Destination
    fields = '__all__'
    template_name = 'destination_create.html'
    success_url = "/destinations/"

class Destination_Detail(DetailView):
    model = Destination
    template_name = 'destination_detail.html'

class Destination_Update(UpdateView):
    model = Destination
    fields = '__all__'
    template_name = 'destination_update.html'
    
    def get_success_url(self):
        return reverse('destination_detail', kwargs={'pk': self.object.pk})

class Destination_Delete(DeleteView):
    model = Destination
    template_name = 'destination_delete_confirmation.html'
    success_url = "/destinations/"

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Hi', user.username)
            return HttpResponseRedirect('/user/' + str(user))
        else:
            return render(request, 'signup.html', {'form':form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})

def profile(request, username):
    user = User.objects.get(username = username)
    return render(request, 'profile.html', {'user':user})
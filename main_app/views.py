from dataclasses import field
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Travel, Itinerary
from .forms import ItineraryForm

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

    # def get(self, request):
    #     return HttpResponse("Travel Planner")

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

class Travel_Detail(DetailView):
    model = Travel
    template_name = 'travel_detail.html'

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
    
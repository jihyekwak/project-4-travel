from re import template
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from .models import Travel

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
            context['header'] = "All Travles"
        return context
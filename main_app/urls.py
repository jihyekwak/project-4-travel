from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('travels/', views.Travel_List.as_view(), name='travel_list'),
    path('travels/new', views.Travel_Create.as_view(), name='travel_create'),
    path('travels/<int:pk>', views.Travel_Detail.as_view(), name='travel_detail')
]
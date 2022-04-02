from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('travels/', views.Travel_List.as_view(), name='travel_list'),
    path('travels/new', views.Travel_Create.as_view(), name='travel_create'),
    path('travels/<int:pk>', views.Travel_Detail.as_view(), name='travel_detail'),
    path('travels/<int:pk>/update', views.Travel_Update.as_view(), name='travel_update'),
    path('travels/<int:pk>/delete', views.Travel_Delete.as_view(), name='travel_delete'),

    path('travels/<int:pk>/itineraries/new', views.Itinerary_Create.as_view(), name='itinerary_create'),
    path('travels/<int:pk>/itineraries/<int:itinerary_id>/update', views.itinerary_update, name='itinerary_update'),
    path('travels/<int:pk>/itineraries/<int:itinerary_id>/delete', views.itinerary_delete, name='itinerary_delete'),

    path('destinations/', views.destination_list, name='destination_list'),
    path('destinations/new', views.Destination_Create.as_view(), name='destination_create'),
    path('destinations/<int:pk>', views.Destination_Detail.as_view(), name='destination_detail'),
    path('destinations/<int:pk>/update', views.Destination_Update.as_view(), name='destination_update'),
    path('destinations/<int:pk>/delete', views.Destination_Delete.as_view(), name='destination_delete'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="loggout"),
    path('signup/', views.signup_view, name="signup")
]
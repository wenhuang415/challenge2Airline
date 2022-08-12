from django.shortcuts import render
from .models import Airline, Aircraft, City, Route
from rest_framework import generics
from .serializers import AirlineSerializer, AircraftSerializer, CitySerializer, RouteSerializer

class AirlineList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

class AircraftList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

class CityList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = City.objects.all()
    serializer_class = CitySerializer

class RouteList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
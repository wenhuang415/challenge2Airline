from django.shortcuts import render
from .models import Airline, Aircraft, City, Route
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AirlineSerializer, AircraftSerializer, CitySerializer, RouteSerializer

class AirlineList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class AircraftList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','speed']

class CityList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class RouteList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cost','distance','origin','destination','aircraft']
from django.shortcuts import render
from .models import Airline
from rest_framework import generics
from .serializers import AirlineSerializer

class AirlineList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer

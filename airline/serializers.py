from rest_framework import serializers
from .models import Airline, Aircraft, City, Route

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields=('aircraft_id','name','speed','airline')

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields=('airline_id','name')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields=('city_id','city_number','county','name','shape_area','shape_length','latitude','longitude')

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields=('route_id','cost','distance','destination','origin','aircraft')
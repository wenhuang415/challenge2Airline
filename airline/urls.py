from django.urls import include, path
from .views import AirlineList, AircraftList, CityList, RouteList


urlpatterns = [
    path('airline', AirlineList.as_view()),
    path('aircraft', AircraftList.as_view()),
    path('city', CityList.as_view()),
    path('route', RouteList.as_view()),
]
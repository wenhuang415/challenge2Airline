from django.urls import include, path
from .views import AirlineList


urlpatterns = [
    path('airline', AirlineList.as_view()),
]
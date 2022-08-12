from django.urls import include, path
from .views import AirlineList


urlpatterns = [
    path('', AirlineList.as_view()),
]
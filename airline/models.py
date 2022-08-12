from django.db import models

# Create your models here.

class Airline(models.Model):
    airline_id = models.CharField(primary_key=True,max_length=240)
    name = models.CharField("Name", max_length=240)

    def __str__(self):
        return self.name
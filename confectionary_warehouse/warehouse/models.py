from django.db import models

from django.core.validators import MinValueValidator
from location.models import City


class Warehouse(models.Model):
    id = models.IntegerField(primary_key=True)
    number_seats = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    cost_seats = models.FloatField(validators=[MinValueValidator(0)], null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    fio = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=25, null=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING)

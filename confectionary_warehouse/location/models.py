from django.db import models


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False)


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Manufacturer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

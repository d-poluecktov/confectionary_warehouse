from rest_framework import serializers

from .models import Country, City, Manufacturer


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField()
    class Meta:
        model = City
        fields = ('id', 'name', 'country_id')


class ManufacturerSerializer(serializers.ModelSerializer):
    city_id = serializers.IntegerField()
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'city_id')

from rest_framework import serializers

from models import Country, City, Manufacturer


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ('id', 'name', 'country')


class ManufacturerSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'city')

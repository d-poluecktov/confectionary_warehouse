from rest_framework import serializers
from location.serializers import CitySerializer
from .models import Warehouse, Employee


class WarehouseSerializer(serializers.ModelSerializer):
    city_id = serializers.IntegerField()

    class Meta:
        model = Warehouse
        fields = ('id', 'number_seats', 'cost_seats', 'city_id')


class EmployeeSerializer(serializers.ModelSerializer):
    warehouse_id = serializers.IntegerField()

    class Meta:
        model = Employee
        fields = ('id', 'fio', 'phone', 'warehouse_id')
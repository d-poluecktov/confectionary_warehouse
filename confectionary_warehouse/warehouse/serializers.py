from rest_framework import serializers
from location.serializers import CitySerializer
from models import Warehouse, Employee


class WarehouseSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Warehouse
        fields = ('id', 'number_seats', 'cost_seats', 'city')


class EmployeeSerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer()

    class Meta:
        model = Employee
        fields = ('id', 'fio', 'phone', 'warehouse')
from rest_framework import serializers
from models import Confectionary


class ConfectionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Confectionary
        fields = (
        'id', 'name', 'weight', 'created_at', 'category', 'expiration_date', 'calory', 'manufacturer', 'customers',
        'warehouses')

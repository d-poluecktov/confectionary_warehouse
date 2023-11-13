import uuid

from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

from location.models import Manufacturer
from warehouse.models import Warehouse
from customer.models import Customer


class Confectionary(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    weight = models.FloatField(validators=[MinValueValidator(1)], null=False)
    created_at = models.DateTimeField(default=timezone.now, null=False)
    category = models.CharField(max_length=255, null=False)
    expiration_date = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=False)
    calory = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=False)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    customers = models.ManyToManyField(Customer)
    warehouses = models.ManyToManyField(Warehouse)

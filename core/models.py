import uuid

from django.db import models


class Order(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    order_code = models.IntegerField(unique=True)
    customer_code = models.IntegerField()


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models

# Create your models here.

# TODO: Implement arrays.
class Product(models.Model):
    name = models.CharField(unique=True, max_length=100)
    price = models.PositiveBigIntegerField()
    quantityAvailable = models.PositiveIntegerField()
    descriptions = models.TextField(null=True)


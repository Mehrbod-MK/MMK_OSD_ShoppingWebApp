from django.db import models

# Create your models here.

## CategoryEnum enumeration.
class CategoryEnum(models.Model):
    name = models.CharField(unique=True, max_length=70)

# TODO: Implement arrays.
class Product(models.Model):
    name = models.CharField(unique=True, max_length=100)
    price = models.PositiveBigIntegerField()
    quantityAvailable = models.PositiveIntegerField()
    descriptions = models.TextField(null=True)
    category = models.ForeignKey(CategoryEnum, on_delete=models.CASCADE, default=0)
    thumbnailImagePath = models.CharField(max_length=256, default='blank')

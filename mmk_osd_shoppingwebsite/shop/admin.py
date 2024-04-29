from django.contrib import admin

# Register your models here.
from .models import Product, CategoryEnum

admin.site.register(Product)
admin.site.register(CategoryEnum)

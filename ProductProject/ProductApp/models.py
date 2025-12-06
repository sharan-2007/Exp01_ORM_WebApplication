from django.db import models
from django.contrib import admin
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100, help_text="Enter the name of the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the price of the product")
    sku = models.TextField(max_length=50, help_text="Enter SKU code")

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'sku')
    
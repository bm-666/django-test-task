from django.contrib import admin
from .models import (
    Product,
    ProductParameters,
    ProductImage
)
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(ProductParameters)
class ParametersAdmin(admin.ModelAdmin):
    ...

@admin.register(ProductImage)
class ImageAdmin(admin.ModelAdmin):
    ...

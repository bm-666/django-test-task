from django.db import models
from . import Product

class ProductParameters(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=20)
    price = models.FloatField()
    product = models.ForeignKey(Product, related_name='params', on_delete=models.CASCADE)

    class Meta:
        db_table = 'parameters'
        verbose_name = 'параметр'
        verbose_name_plural = 'параметры'
        ordering = ('name', 'price')

    def __str__(self):
        return self.name

from django.core.files.images import ImageFile
from django.db import models
from . import Product

class ProductImage(models.Model):
        file = models.ImageField()
        title = models.CharField(max_length=100)
        product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

        class Meta:
            db_table = 'images'
            verbose_name = 'изображение'
            verbose_name_plural = 'изображения'
            ordering = ('title',)

        def __str__(self):
            return self.title

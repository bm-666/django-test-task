from rest_framework import serializers
from ..models import ProductParameters

class ProductParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductParameters
        fields = ('name', 'value', 'price')

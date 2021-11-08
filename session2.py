# coding: utf-8
from backend.models import Product
from backend.api.serializers import ProductSerializer
product = Product.objects.get(pk='KKK-1')
product
serializer = ProductSerializer(product)
serializer.data

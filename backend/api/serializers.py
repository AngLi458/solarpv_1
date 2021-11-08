from rest_framework import serializers
from ..models import Product
from ..models import Certificate
from ..models import Service

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product
        fields = ['model_num', 'name', 'cell_technology', 'num_cells', 'product_weight']

class CertificateSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Certificate
        fields = ['certificate_id', 'cert_num', 'location']

class ServiceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Service
        fields = ['service_id', 'service_name', 'description']

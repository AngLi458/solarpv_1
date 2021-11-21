from rest_framework import serializers
from ..models import Product
from ..models import Certificate
from ..models import Service

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product
        fields = ['model_num', 'name', 'cell_technology', 'num_cells', 'product_weight']

class CertificateSerializer(serializers.ModelSerializer): 
    location_address = serializers.CharField(source='location.address1', read_only=True)
    location_city = serializers.CharField(source='location.city', read_only=True)
    location_state = serializers.CharField(source='location.state', read_only=True)
    location_country = serializers.CharField(source='location.country', read_only=True)
    contact_first_name = serializers.CharField(source='contact.first_name', read_only=True)
    contact_last_name = serializers.CharField(source='contact.last_name', read_only=True)
    test_standard_name = serializers.CharField(source='test_standard.standard_name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    class Meta: 
        model = Certificate
        fields = ['certificate_id', 'cert_num', 'location_address', 'location_city', 'location_state', 'location_country', 'report_num', 'contact_first_name', 'contact_last_name', 'test_standard_name', 'product_name', 'cert_issue_date']

class ServiceSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Service
        fields = ['service_id', 'service_name', 'description']

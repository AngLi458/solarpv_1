from rest_framework import generics
from ..models import Product
from ..models import Certificate
from ..models import Service
from .serializers import ProductSerializer
from .serializers import CertificateSerializer
from .serializers import ServiceSerializer
from rest_framework import filters

class ProductListView(generics.ListAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
        
class CertificatetListView(generics.ListAPIView): 
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cert_num', 'location__address1', 'location__city', 'location__state', 'location__country', 'contact__first_name', 'contact__last_name', 'test_standard__standard_name', 'product__name', 'cert_issue_date']

class CertificateDetailView(generics.RetrieveAPIView): 
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer
        
class ServiceListView(generics.ListAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

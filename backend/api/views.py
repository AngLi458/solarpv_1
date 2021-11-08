from rest_framework import generics
from ..models import Product
from ..models import Certificate
from ..models import Service
from .serializers import ProductSerializer
from .serializers import CertificateSerializer
from .serializers import ServiceSerializer
class ProductListView(generics.ListAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
        
class CertificatetListView(generics.ListAPIView): 
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer

class CertificateDetailView(generics.RetrieveAPIView): 
    queryset = Certificate.objects.all() 
    serializer_class = CertificateSerializer
        
class ServiceListView(generics.ListAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView): 
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer
        

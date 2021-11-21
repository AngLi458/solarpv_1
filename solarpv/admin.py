from django.contrib import admin

# Register your models here.

from backend.models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin): 
    list_display = ['client_id', 'client_code', 'client_name', 'client_type'] 
    list_filter = ['client_name', 'client_code'] 
    search_fields = ['client_code', 'client_name']
    

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin): 
    list_display = ['location_id', 'client', 'address1', 'address2', 'city', 'state', 'postal_code', 'country', 'phone_number', 'fax_number'] 
    list_filter = ['client', 'city', 'state', 'country'] 
    search_fields = ['city', 'country', 'address1']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    fieldsets = (
        (None, {
                        'fields': ('model_num', 'name', 'cell_technology', 'cell_manufacturer', 'num_cells', 'num_cells_in_series', 'num_diodes', 'product_length', 'product_width', 'product_weight')
                    
        }),
        ('Advanced options', {
                        'classes': ('collapse',),
                        'fields': ('superstrate_type', 'superstrate_manufacturer', 'substrate_type', 'substrate_manufacturer', 'frame_type', 'frame_adhesive', 'encapsulant_type', 'encapsulant_manufacturer', 'junction_box_type', 'junction_box_manufacturer'),
                    
        }),
    )
    list_display = ['model_num', 'name', 'num_cells', 'num_cells_in_series', 'cell_technology', 'cell_manufacturer']
    list_filter = ['cell_technology', 'cell_manufacturer'] 
    search_fields = ['model_num', 'name']


@admin.register(Test_standard)
class TestStandardAdmin(admin.ModelAdmin): 
    list_display = ['standard_id', 'standard_name', 'description', 'published_date'] 
    search_fields = ['standard_name', 'description']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin): 
    list_display = ['certificate_id', 'cert_num', 'location', 'report_num', 'contact', 'test_standard', 'product', 'cert_issue_date'] 
    list_filter = ['contact', 'product', 'cert_issue_date'] 
    search_fields = ['cert_num', 'report_num', 'cert_issue_date']

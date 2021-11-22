# coding: utf-8
#get_ipython().run_line_magic('load', 'session1')
import django
django.setup()
# %load session1
from backend.models import *
User.objects.all()
# create client objects
q = Client(client_code='SLR', client_name='Solaria Corporation', client_type='company')
q.save()
q = Client(client_code='MRC', client_name='Mine Radio Cici', client_type='company')
q.save()
q = Client(client_code='TEL', client_name='Tesla company', client_type='company')
q.save()
# query client object using exclude and delete client objects
#Client.objects.all()
#Client.objects.exclude(client_id=1).delete()
#Client.objects.filter(client_id=3).delete()
#Client.objects.all()
# obtain client object
q = Client.objects.get(pk=1)
# create User object
u = User(client=q, user_id='liangliang', first_name='Ang', middle_name='', last_name='Li', job_title='ceo', email='angli@asu', office_phone='111-222-3333', cell_phone='333-444-5555', prefix='Mr.', is_staff='y')
u.save()
q = Client.objects.get(pk=2)
u = User(client=q, user_id='liangliang1', first_name='Angg', middle_name='', last_name='Li', job_title='ceo', email='angli@asu', office_phone='111-222-3333', cell_phone='333-444-5555', prefix='Mr.', is_staff='y')
u.save()
q = Client.objects.get(pk=3)
u = User(client=q, user_id='liangliang2', first_name='Anggg', middle_name='', last_name='Li', job_title='ceo', email='angli@asu', office_phone='111-222-3333', cell_phone='333-444-5555', prefix='Mr.', is_staff='y')
u.save()
# use exclude to query user objects and delete user objects
#User.objects.exclude(user_id=1).delete()
u = User.objects.get(user_id='liangliang')

# obtain client object
q = Client.objects.get(pk=1)
# create location object
l = Location(client=q, address1='22 happy street', address2='23 new york street', 
             city='NY', state='LA', postal_code='kkk nnn', country='US', 
             phone_number='555-666-7777', fax_number='999-000-1111')
l.save()

# query location object and update its address
l = Location.objects.get(pk=1)
l.address1 = '33 happy street'
l.save()

q = Client.objects.get(pk=2)
# create location object
l = Location(client=q, address1='35 sad street', address2='28 us street', 
             city='NY', state='LA', postal_code='lll bbb', country='US', 
             phone_number='553-123-0089', fax_number='999-000-1111')
l.save()

# create product object

product = Product(model_num='KKK-1', name='product1', cell_technology='cell_t', cell_manufacturer='cell_m', num_cells=10, num_cells_in_series=20, num_series_strings=1000, num_diodes=200, product_length=1001.2, product_width=33.3, product_weight=10001.5, superstrate_type='sup_t', superstrate_manufacturer='sup_m', substrate_type='sub_t', substrate_manufacturer='sub_m', frame_type='ft', frame_adhesive=10.1, encapsulant_type='en_t', encapsulant_manufacturer='en_m', junction_box_type='jbt', junction_box_manufacturer='jbm')
product.save()

product = Product(model_num='KKK-2', name='product2', cell_technology='cell_t', cell_manufacturer='cell_m', num_cells=10, num_cells_in_series=20, num_series_strings=1000, num_diodes=200, product_length=1001.2, product_width=33.3, product_weight=10001.5, superstrate_type='sup_t', superstrate_manufacturer='sup_m', substrate_type='sub_t', substrate_manufacturer='sub_m', frame_type='ft', frame_adhesive=10.1, encapsulant_type='en_t', encapsulant_manufacturer='en_m', junction_box_type='jbt', junction_box_manufacturer='jbm')
product.save()

#query location, product, and user objects
l = Location.objects.get(pk=1)
p = Product.objects.get(pk='KKK-1')
u = User.objects.get(pk='liangliang')

#create product_factory object
pf = Product_factory(location=l, product=p, contact=u)
pf.save()

test = Test_standard(standard_name='standard1', description='description of test', published_date='2021-11-07')
test.save()

cert = Certificate(cert_num='CA 72180017', location=l, report_num='report1', contact=u, test_standard=test, product=p, cert_issue_date='2021-11-09')

cert.save()

l = Location.objects.get(pk=2)
p = Product.objects.get(pk='KKK-2')
u = User.objects.get(pk='liangliang1')

cert = Certificate(cert_num='AD 1823953', location=l, report_num='report2', contact=u, test_standard=test, product=p, cert_issue_date='2021-11-09')

cert.save()

serv = Service(service_name='service1', description='service description', is_fi_required='n', fi_frequency=0.0, test_standard=test)

serv.save()

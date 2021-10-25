# coding: utf-8
get_ipython().run_line_magic('load', 'session1')
# %load session1
from backend.models import *
User.objects.all()
# create client objects
q = Client(client_code='001', client_name='client1', client_type='manager')
q.save()
q = Client(client_code='002', client_name='client2', client_type='employee')
q.save()
q = Client(client_code='003', client_name='client3', client_type='worked')
q.save()
# query client object using exclude and delete client objects
Client.objects.all()
Client.objects.exclude(client_id=1).delete()
#Client.objects.filter(client_id=3).delete()
#Client.objects.all()
# obtain client object
q = Client.objects.get(pk=1)
# create User object
u = User(client=q, first_name='Ang', middle_name='', last_name='Li', job_title='ceo', email='angli@asu', office_phone='111-222-3333', cell_phone='333-444-5555', prefix='Mr.', is_staff='y')
u.save()
u = User(client=q, first_name='Angg', middle_name='', last_name='Li', job_title='ceo', email='angli@asu', office_phone='111-222-3333', cell_phone='333-444-5555', prefix='Mr.', is_staff='y')
u.save()
u = User(client=q, first_name='Anggg', middle_name='', last_name='Li', job_title='ceo', email='angli@asu', office_phone='111-222-3333', cell_phone='333-444-5555', prefix='Mr.', is_staff='y')
u.save()
# use exclude to query user objects and delete user objects
User.objects.exclude(user_id=1).delete()

# obtain client object
q = Client.objects.get(pk=1)
# create location object
l = Location(client=q, address1='22 happy street', address2='23 new york street', city='NY', state='LA', postal_code='kkk nnn', country='US', phone_number='555-666-7777', fax_number='999-000-1111')
l.save()

# query location object and update its address
l = Location.objects.get(pk=1)
l.address1 = '33 happy street'
l.save()

# create product object

product = Product(model_num='KKK-1', name='product1', cell_technology='cell_t', cell_manufacturer='cell_m', num_cells=10, num_cells_in_series=20, num_series_strings=1000, num_diodes=200, product_length=1001.2, product_width=33.3, product_weight=10001.5, superstrate_type='sup_t', superstrate_manufacturer='sup_m', substrate_type='sub_t', substrate_manufacturer='sub_m', frame_type='ft', frame_adhesive=10.1, encapsulant_type='en_t', encapsulant_manufacturer='en_m', junction_box_type='jbt', junction_box_manufacturer='jbm')
product.save()

#query location, product, and user objects
l = Location.objects.get(pk=1)
p = Product.objects.get(pk='KKK-1')
u = User.objects.get(pk=1)

#create product_factory object
pf = Product_factory(location=l, product=p, contact=u)
pf.save()

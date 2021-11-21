from django.db import models

# Create your models here.

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_code = models.CharField(max_length=10)
    client_name = models.CharField(max_length=20)
    client_type = models.CharField(max_length=20)

class User(models.Model):
    user_id = models.CharField(max_length=20, primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    job_title = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    office_phone = models.CharField(max_length=15)
    cell_phone = models.CharField(max_length=15)
    prefix = models.CharField(max_length=10)
    is_staff = models.CharField(max_length=1)

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    fax_number = models.CharField(max_length=15)

    def __str__(self):
        return self.address1

class Test_standard(models.Model):
    standard_id = models.AutoField(primary_key=True)
    standard_name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.standard_name

class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    is_fi_required = models.CharField(max_length=1)
    fi_frequency = models.FloatField()
    test_standard = models.ForeignKey(Test_standard, on_delete=models.CASCADE)

class Product(models.Model):
    model_num = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    cell_technology = models.CharField(max_length=20)
    cell_manufacturer = models.CharField(max_length=20)
    num_cells = models.IntegerField()
    num_cells_in_series = models.IntegerField()
    num_series_strings = models.IntegerField()
    num_diodes = models.IntegerField()
    product_length = models.FloatField()
    product_width = models.FloatField()
    product_weight = models.FloatField()
    superstrate_type = models.CharField(max_length=20)
    superstrate_manufacturer = models.CharField(max_length=20)
    substrate_type = models.CharField(max_length=20)
    substrate_manufacturer = models.CharField(max_length=20)
    frame_type = models.CharField(max_length=20)
    frame_adhesive = models.FloatField()
    encapsulant_type = models.CharField(max_length=20)
    encapsulant_manufacturer = models.CharField(max_length=20)
    junction_box_type = models.CharField(max_length=20)
    junction_box_manufacturer = models.CharField(max_length=20)


class Test_sequence(models.Model):
    sequence_id = models.AutoField(primary_key=True)
    sequence_name = models.CharField(max_length=20)

class Performance_data(models.Model):
    model_num = models.ForeignKey(Product, on_delete=models.CASCADE)
    sequence = models.ForeignKey(Test_sequence, on_delete=models.CASCADE)
    msv = models.FloatField()
    voc = models.FloatField()
    isc = models.FloatField()
    vmp = models.FloatField()
    imp = models.FloatField()
    pmp = models.FloatField()
    ff = models.FloatField()

class Product_factory(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    contact = models.ForeignKey(User, on_delete=models.CASCADE)

class Certificate(models.Model):
    certificate_id = models.AutoField(primary_key=True)
    cert_num = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    report_num = models.CharField(max_length=20)
    contact = models.ForeignKey(User, on_delete=models.CASCADE)
    test_standard = models.ForeignKey(Test_standard, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cert_issue_date = models.DateTimeField()

    def __str__(self):
        return self.cert_num

class Factory_inspection(models.Model):
    factory_inspection_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    report_num = models.CharField(max_length=20)
    date = models.DateTimeField()
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    inspection_sqeuence = models.CharField(max_length=20)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    finding = models.CharField(max_length=300)

class Expertise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_standard = models.ForeignKey(Test_standard, on_delete=models.CASCADE)
    certification = models.CharField(max_length=20)

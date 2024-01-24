
from django.db import models

# class Client(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.TextField()
#     email = models.EmailField()
#     tax_number = models.CharField(max_length=50)

class Invoice(models.Model):
    client_name = models.CharField(max_length=100)
    client_address = models.TextField()
    client_gstin = models.CharField(max_length=50)
    client_contact_details = models.CharField(max_length=100)
    client_country = models.CharField(max_length=50,default='NA')
    client_statecode = models.CharField(max_length=100,default='NA')
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)
    invoice_no= models.CharField(max_length=50, primary_key=True)
    invoice_date = models.DateField()
    # incremental_invoice_number = models.CharField(max_length=20)
    service_accounting_code = models.CharField(max_length=20)
    description_of_service = models.CharField(max_length=255)
    hours_units = models.DecimalField(max_digits=10, decimal_places=2)
    value_usd = models.DecimalField(max_digits=10, decimal_places=2)
    taxable_value_inr = models.DecimalField(max_digits=10, decimal_places=2)
    tax= models.CharField(max_length=50,default=0)
    total_amount= models.CharField(max_length=50,default=0)


    def __str__(self):
        return self.invoice_no

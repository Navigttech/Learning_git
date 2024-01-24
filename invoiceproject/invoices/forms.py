# from django import forms
# from .models import Invoice

# class InvoiceForm(forms.ModelForm):
#     class Meta:
#         model = Invoice
#         fields = ['customer_name']  # Add other fields here


import datetime

from django import forms
from .models import Invoice

class Invoice(forms.ModelForm):
    # client_name = forms.CharField()
    # client_address = forms.CharField(widget=forms.Textarea)
    # client_gstin = forms.CharField()
    # client_contact_details = forms.CharField()
    # invoice_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), initial=datetime.date.today)

    # # client = forms.ModelChoiceField(queryset=Client.objects.all(), empty_label="Select Client")

    # invoice_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    # # incremental_invoice_number = forms.CharField()
    
    # service_accounting_code=forms.CharField()
    # description_of_service=forms.CharField()
    # hours_units=forms.CharField()
    # taxable_value_inr=forms.CharField()
    # tax=forms.CharField()
    # Total_in_words=forms.CharField()

    class Meta:
        model = Invoice
        fields = ['client_name','client_address','client_gstin','client_contact_details','client_country','client_statecode','invoice_no','invoice_date','service_accounting_code', 'description_of_service', 'hours_units', 'value_usd', 'taxable_value_inr','tax','total_amount']

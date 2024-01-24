# Create your views here.
from django.shortcuts import render, redirect
from .models import Invoice
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from django.contrib import messages

def create_invoice(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_address = request.POST.get('client_address')
        client_gstin =request.POST.get('client_gstin')
        client_contact_details = request.POST.get('client_contact_details')
        client_country =request.POST.get('client_country')
        client_statecode =request.POST.get('client_statecode')
        invoice_no=request.POST.get('invoice_no')
        invoice_date = request.POST.get('invoice_date')
        service_accounting_code = request.POST.get('service_accounting_code')
        description_of_service = request.POST.get('description_of_service')
        hours_units =request.POST.get('hours_units')
        value_usd = request.POST.get('value_usd')
        taxable_value_inr =request.POST.get('taxable_value_inr')
        tax=request.POST.get('tax')
        total_amount=request.POST.get('total_amount')

        inv=Invoice(client_name=client_name,
                        client_address =client_address , 
                        client_gstin= client_gstin,
                        client_contact_details=client_contact_details,
                        client_country= client_country,
                        client_statecode= client_statecode,
                        invoice_no=invoice_no,
                        invoice_date=invoice_date,
                        service_accounting_code=service_accounting_code,
                        description_of_service=description_of_service,
                        hours_units=hours_units,
                        value_usd = value_usd ,
                        taxable_value_inr=taxable_value_inr,
                        tax=tax,
                        total_amount=total_amount)
        # inv=InvoiceForm()
        inv.save()
        messages.success(request, "Invoices is successfully saved.")
    
        # return redirect('http://127.0.0.1:8000/invoice_details', invoice_id=inv.invoice_no)
        # return render(request,'invoice_details')
        return redirect(view_invoice_details, invoice_id=inv.invoice_no)
        # return HttpResponse("i am being redirected")
        #  , invoice_id=inv.invoice_no)
       
    return render(request, 'create_invoice.html')    
# def create_invoice(request):
#     if request.method == 'POST':
#         form = InvoiceForm(request.POST)
#         if form.is_valid():
#             invoice_data = form.cleaned_data  # Use cleaned_data to get the form data
#             try:
#                 form.save()
#                 pdf_response = generate_pdf(invoice_data)
#                 return pdf_response
#             except Exception as e:
#                 print(f"An error occurred: {e}")
#             # form.save()
#             # # Add code to generate PDF here
#             # return redirect('invoice_success')  # Create a success page
#     else:
#         form = InvoiceForm()
#     return render(request, 'create_invoice.html', {'form': form})



def view_invoice_details(request, invoice_id):
    # Retrieve the invoice details from the database using the invoice_id
    # return HttpResponse("i am being redirected")
    # invoice = Invoice.objects.get(pk=invoice_id)
    # return render(request, 'invoice_details.html', {'invoice': invoice})
    try:
        invoice = Invoice.objects.get(invoice_no=invoice_id)
        return render(request, 'invoice_details.html', {'invoice': invoice})
    except Invoice.DoesNotExist:
        return render(request, 'invoice_not_found.html')
from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    # path('', admin.site.urls, name='create_invoice'),
    path('',views.create_invoice, name='createform_invoice'),
    path('submit',views.create_invoice, name='createform_invoice'),
    path('create_invoice',views.create_invoice,name="postrequest"),
    # path('print_invoice',views.print_invoice,name='print_invoice'),
    path('invoice_details/<str:invoice_id>/', views.view_invoice_details, name='view_invoice_details'),
    # path('http://127.0.0.1:8000/invoice_details/<str:invoice_id>/',views.view_invoice_details, name='view_invoice_details')
]
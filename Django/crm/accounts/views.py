from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders=orders.count()
    delivered=orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context={'orders':orders,'customers':customers,'total_orders':total_orders,
             'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)
def products(request):
    product=Product.objects.all()
    return render(request,'accounts/products.html',{'products':product})
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    total_orders = customer.order_set.all().count()
    orders = customer.order_set.all()
    context={'customer':customer,'total_orders':total_orders,'orders':orders}
    return render(request,'accounts/customer.html',context)
def createOrder(request):
    context = {}
    return render(request,'accounts/order_form.html',context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from . models import *
from .form import OrderForm
from .filters import OrderFilter
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders=orders.count()
    #cus = Customer.objects.get(id=1)
    orders_filter = orders.all()
    myFilter = OrderFilter(request.GET,queryset=orders_filter)
    orders_filter=myFilter.qs
    delivered=orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context={'orders':orders_filter,'customers':customers,'total_orders':total_orders,
             'delivered':delivered,'pending':pending,'filter':myFilter}
    return render(request,'accounts/dashboard.html',context)
def products(request):
    product=Product.objects.all()
    return render(request,'accounts/products.html',{'products':product})
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    total_orders = customer.order_set.all().count()
    orders = customer.order_set.all()
    filter = OrderFilter(request.GET,queryset=orders)
    orders = filter.qs
    context={'customer':customer,'total_orders':total_orders,'orders':orders,'filter':filter}
    return render(request,'accounts/customer.html',context)
def createMultipleOrder(request,pk):
    customer = Customer.objects.get(id=pk)
    orderform = inlineformset_factory(Customer,Order, fields=('product','quantity'),extra=10)
    formset = orderform(instance=customer)
    #form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = orderform(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset}
    return render(request,'accounts/order_multiple_form.html',context)
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/order_form.html',context)
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
    return redirect('/')
def updateOrderCus(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/order_form.html',context)
def deleteOrderCus(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
    return redirect('/')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import *
from .form import OrderForm,OrderFilter,CreateUserForm
# Create your views here.
@login_required(login_url='login')
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
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    context ={'form':form}
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'User Account has been created for ' + user)
            return redirect('login')
        else:
            messages.error(request,"Fill all therequired fields")
            return redirect('registration')
    return render(request,'accounts/registration.html',context)
def Userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        context={}
        if request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Username or Password is incorrect!")
        return render(request,'accounts/login.html',context)
def Userlogout(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def products(request):
    product=Product.objects.all()
    return render(request,'accounts/products.html',{'products':product})
@login_required(login_url='login')
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    total_orders = customer.order_set.all().count()
    orders = customer.order_set.all()
    filter = OrderFilter(request.GET,queryset=orders)
    orders = filter.qs
    context={'customer':customer,'total_orders':total_orders,'orders':orders,'filter':filter}
    return render(request,'accounts/customer.html',context)
@login_required(login_url='login')
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
@login_required(login_url='login')
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
@login_required(login_url='login')
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
    return redirect('/')
@login_required(login_url='login')
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
@login_required(login_url='login')
def deleteOrderCus(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
    return redirect('/')


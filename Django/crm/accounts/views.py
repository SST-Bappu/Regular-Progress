from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.forms import inlineformset_factory

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from . models import *
from .form import *
from .decorator import *
# Create your views here.
@login_required(login_url='login')
@admin_only
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
#@unauthenticated_user
def register(request):
    form = CreateUserForm()
    context ={'form':form}
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            '''group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user = user,
            )'''
            messages.success(request,'User Account has been created for ' + username)
            return redirect('login')
        else:
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            if pass1 != pass2:
                messages.error(request,"Password didn't match")
            else:
                messages.error(request,"Fill all the required fields correctly")
            return redirect('registration')
    return render(request,'accounts/registration.html',context)
@unauthenticated_user
def Userlogin(request):
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
@login_required(login_url="login")
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method=='POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context ={'form':form}
    return render(request,'accounts/account_settings.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def UserAccountSettingsbyAdmin(request,pk_test): #To give the admin the ability to change the user account settings if needed
    customer = Customer.objects.get(id=pk_test)
    #customer = cust.user
    form = CustomerForm(instance=customer)
    if request.method=='POST':
        form = CustomerForm(request.POST,request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'accounts/account_settings.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    product=Product.objects.all()
    return render(request,'accounts/products.html',{'products':product})
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    total_orders = customer.order_set.all().count()
    orders = customer.order_set.all()
    filter = OrderFilter(request.GET,queryset=orders)
    orders = filter.qs
    context={'customer':customer,'total_orders':total_orders,'orders':orders,'filter':filter}
    return render(request,'accounts/customer.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage (request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    customers = request.user.customer
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count
    cusFilter = OrderFilter(request.GET,queryset=orders)
    orders = cusFilter.qs
    context={'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,
             'pending':pending,'filter':cusFilter}
    return render(request,'accounts/user.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def AddProducts(request):
    form = AddProductsForm()
    if request.method=='POST':
        form = AddProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {'form':form}
    return render(request,'accounts/addProducts.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
    return redirect('/')
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrderCus(request,pk):
    order = Order.objects.get(id=pk)
    id = order.customer.id
    form = OrderForm(instance=order)
    if request.method =='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('customer',pk_test=id)
    context={'form':form}
    return render(request,'accounts/order_form.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrderCus(request,pk):
    order = Order.objects.get(id=pk)
    id = order.customer.id
    if request.method=="POST":
        order.delete()
    return redirect('customer',pk_test=id)


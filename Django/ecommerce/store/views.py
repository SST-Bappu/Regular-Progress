from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    products = Product.objects.all()
    context ={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = 0
    context ={'items':items,'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.get(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context ={'items':items,'order':order}
    return render(request,'store/checkout.html',context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("Product ID=",productId)
    print("Action = ",action)
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item,created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        order_item.quantity +=1
    elif action=='remove':
        order_item.quantity -=1
    order_item.save()
    if order_item.quantity<=0:
        order_item.delete()
    return JsonResponse("Data is added",safe=False)
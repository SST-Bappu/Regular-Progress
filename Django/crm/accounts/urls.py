from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('products/',views.products,name="products"),
    path('customer/<str:pk_test>/',views.customer,name="customer"),
    path('createMultipleOrder/<str:pk>/',views.createMultipleOrder,name="createMultipleOrder"),
    path('updateOrder/<str:pk>/',views.updateOrder,name="updateOrder"),
    path('deleteOrder/<str:pk>/',views.deleteOrder,name="deleteOrder"),
    path('updateOrderCus/<str:pk>/',views.updateOrderCus,name="updateOrderCus"),
    ]
 
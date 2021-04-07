from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('products/',views.products,name="products"),
    path('customer/<str:pk_test>/',views.customer,name="customer"),
    path('createMultipleOrder/<str:pk>/',views.createMultipleOrder,name="createMultipleOrder"),
    path('updateOrder/<str:pk>/',views.updateOrder,name="updateOrder"),
    path('deleteOrder/<str:pk>/',views.deleteOrder,name="deleteOrder"),
    path('updateOrderCus/<str:pk>/',views.updateOrderCus,name="updateOrderCus"),
    path('deleteOrderCus/<str:pk>/',views.deleteOrderCus,name="deleteOrderCus"),
    path('register/',views.register,name="registration"),
    path('login/',views.Userlogin,name="login"),
    path('logout/',views.Userlogout,name='logout'),
    path('userPage/',views.userPage,name='userPage'),
    path('accountSettings/',views.accountSettings,name="settings"),
    path('UserAccountSettingsByAdmin/<str:pk_test>/',views.UserAccountSettingsbyAdmin,name='settings_admin'),
    path('addProducts/',views.AddProducts,name='addProducts'),

    #Using Default Django Reset Password templates and views
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name='password_reset_complete'),
    ]
 
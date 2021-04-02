from django.forms import ModelForm
from django import forms
import django_filters
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('customer','product','quantity','status')
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control','step':"0.5"}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }
class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields = '__all__'#('customer','product','date','status')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
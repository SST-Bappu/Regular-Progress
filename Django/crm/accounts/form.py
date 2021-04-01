from django.forms import ModelForm
from django import forms
from .models import Order

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
from django import forms
from .models import Order, OrderPickup


class OrderPickupForm(forms.ModelForm):
    class Meta:
        model = OrderPickup
        fields = ['first_name', 'last_name', 'phone_number', ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'postal_code', 'city', 'phone_number', ]

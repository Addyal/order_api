from django import forms
from .models import Order

# user form for order details 
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'address1', 'address2', 'town_city', 'postcode']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'town_city': 'Town or City',
        }
from django import forms
from .models import Order, Customer

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'address1', 'address2', 'town_city', 'postcode']
        labels = {
            'town_city': 'Town or City',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()
        self.fields['customer'].label_from_instance = lambda obj: f"{obj.name} - {obj.email}"

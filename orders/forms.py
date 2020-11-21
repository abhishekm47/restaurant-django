from django import forms
from .models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['resto_type','order_type','first_name', 'last_name', 'email', 
                  'address', 'postal_code', 'city', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'first Name'}),
            'resto_type': forms.RadioSelect(attrs={'label': 'Select our restaurant branch'}),
            'order_type': forms.RadioSelect(attrs={'label': 'Select your order type'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'address': forms.TextInput(attrs={'placeholder': 'address'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Postal code'}),
            'city': forms.TextInput(attrs={'placeholder': 'city'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'contact number'}),
                               
        }
    
class OrderUpdateForm(forms.ModelForm):
    'status'
    class Meta:
        model = OrderItem
        fields = ['price', 'quantity', 'status', 'time']




       




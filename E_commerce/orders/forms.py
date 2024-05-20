from django import forms
from .models import Order

class Orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','phone','email','address_first','address_second','country','state','city','order_note']
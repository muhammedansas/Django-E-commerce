from django.shortcuts import render,redirect
from cart.models import Cartitem
from .forms import Orderform
from .models import Order
import datetime

# Create your views here.

def place_order(request,grand_total=0,tax=0):
    current_user = request.user

    #if the  cart count is less than or equal to 0 then redirect back to shop
    cart_items = Cartitem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')
    total = 0
    grand_total = 0
    tax = 0
    quantity = 0
    for i in cart_items:
        total += (i.product.price*i.quantity)
        quantity += i.quantity
    tax = (2 * total)/100
    grand_total = total + tax    
    
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.address_first = form.cleaned_data['address_first']
            data.address_second = form.cleaned_data['address_second']
            data.country = form.cleaned_data['country']
            data.state = form.cleaned_data['state']
            data.city = form.cleaned_data['city']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            #generate order number
            day = int(datetime.date.today().strftime('%D'))
            month = int(datetime.date.today().strftime('%M'))
            year = int(datetime.date.today().strftime('%Y'))
            d = datetime.date(day,month,year)
            current_date = d.strftime('%Y%M%D')
            order_number = current_date + str(data.id)
            data.oreder_number = order_number
            data.save()
            return redirect('checkout')
        else:
            return redirect('checkout')
        
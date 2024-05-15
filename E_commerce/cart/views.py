from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product
from . models import Cart,Cartitem
from django.contrib.auth.decorators import login_required

# Create your views here.

def cart_id(request):
    cart = request.session.session_key          # if there is a existing session so this will work
    if not cart:
        cart = request.session.create()          # if there is no session so this will create one
    return cart

@login_required(login_url='login')
def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)  # to get the product

    try:
        cart = Cart.objects.get(cart_id = cart_id(request))  # get the cart using the cart id present in tne session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = cart_id(request)
        )
        cart.save()

    try:
        cart_item = Cartitem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except Cartitem.DoesNotExist:
        cart_item = Cartitem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product, id = product_id)
    cart_item = Cartitem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    product = get_object_or_404(Product,id=product_id)  
    cart_item = Cartitem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart')  


@login_required(login_url='login')
def cart(request,total=0,quantity=0,cart_items=None,):
    tax = None
    grand_total = None
    try:
        cart = Cart.objects.get(cart_id = cart_id(request))
        cart_items = Cartitem.objects.filter(cart=cart,is_active = True)
        for items in cart_items:
            total += (items.product.price * items.quantity)
            quantity += items.quantity
        tax = (2 * total)/100
        grand_total = total + tax    
    except:
        print('its wrong')
        pass    # just ignore

    context = {
        "total" : total,
        "quantity" : quantity,
        "cart_items" : cart_items,
        "tax" : tax,
        "grand_total" : grand_total
    }          
    return render(request,'Home/cart.html',context)

def checkout(request):
    return render(request,'Home/checkout.html')
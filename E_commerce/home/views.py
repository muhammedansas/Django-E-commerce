from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from orders.models import Order

# Create your views here.

def home(request):
    product = Product.objects.all()
    return render(request, 'Home/home.html',{'products':product})

def dashboard(request):
    order = Order.objects.order_by('-created_at').filter(user=request.user,is_ordered=True)
    orders_count = order.count()
    context = {
        "order":order,
        "orders_count":orders_count
    }
    return render(request,"Home/dashboard.html",context)

def orders(request):    
    orders = Order.objects.filter(user = request.user,is_ordered = True).order_by()
    context = {"orders":orders}
    return render(request,"Home/orders.html",context)
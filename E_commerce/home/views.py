from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import Product
from orders.models import Order
from accounts.models import Account
from django.contrib import messages

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

def change_password(request):
    if request.POST:
        current_password = request.POST["current_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]

        user = Account.objects.get(username__iexact = request.user.username)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                messages.success(request,"Password updated successfully")
                return redirect('change_password')
            else:
                messages.error(request,"Please enter valid current password")
                return redirect('dashboard')
        else:
            messages.error(request,"Password does not match")
            return redirect("dashboard")        
        
    return render(request,'Home/change_password.html')
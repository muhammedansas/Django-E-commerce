from django.shortcuts import render,redirect
from accounts.models import Account,Userprofile
from store.models import Product
from products_category.models import catogary
from . forms import Product_update_form,Category_update_form
from django.contrib import messages
from orders.models import Order
# Create your views here.

def admin_panel(request):
  
    return render(request,'admin_panel/admin.html') 

def admin_users(request):
    users = Account.objects.all()
    context={
        "users":users
    }
    return render(request,"admin_panel/admin_users.html",context)

def admin_category(request):
    categories = catogary.objects.all().order_by("id")
    print(categories,"hi helooooo")
    context = {"categories":categories}
    return render(request,"admin_panel/admin_category.html",context)

def admin_products(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request,"admin_panel/admin_products.html",context)

def add_product(request):
    form = None
    if request.method =="POST":
        form = Product_update_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_products')
        else:
            form = Product_update_form()
            print("helloo patichee")
    context = {
        "form":form
    }
    return render(request,"admin_panel/add_product.html",context)

def edit_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = Product_update_form(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_products')
    else:
        form = Product_update_form(instance = product)
    context = {
        "form":form
    }    
    return render(request, "admin_panel/add_product.html",context)


def delete_product(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('admin_products')

def admin_category(request):
    category = catogary.objects.all()
    context = { 
        "category":category
    }
    return render(request,"admin_panel/admin_category.html",context)

def add_category(request):
    if request.method == "POST":
        form = Category_update_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("admin_category")
    else:
        form = Category_update_form()
    context = {"form":form} 
    return render(request,"admin_panel/category_update_form.html",context)  

def edit_category(request,slug):
    category = catogary.objects.get(slug=slug)
    if request.method == "POST":
        form = Category_update_form(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.success(request,"Category successfully edited")
            return redirect("admin_category")
    else:
        form = Category_update_form(instance=category)
    context = {"form":form}        
    return render(request,"admin_panel/category_update_form.html",context)

def delete_category(request,slug):
    category = catogary.objects.get(slug=slug)
    category.delete()
    messages.success(request,"Category successfully deleted")
    return redirect("admin_category")

def admin_userprofile(request,id):
    users = Account.objects.get(id=id)
    user = Userprofile.objects.get(user=users)
    print(user,"asdfghjk")
    context = {
        "user":user
    }
    return render(request,"admin_panel/admin_userprofile.html",context)

def admin_orders(request):
    orders = Order.objects.filter(is_ordered=True).order_by()
    context={"orders":orders}
    return render(request,"admin_panel/admin_orders.html",context)
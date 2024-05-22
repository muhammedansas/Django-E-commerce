from django.shortcuts import render,redirect
from accounts.models import Account,Userprofile
from store.models import Product
from products_category.models import catogary
from . forms import Product_update_form
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
    categories = catogary.objects.all()
    
    return

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
    context = {
        "form":form
    }
    return render(request,"admin_panel/add_product.html",context)

def edit_product(request,id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = Product_update_form(request.POST, request.FILES, instance=product)
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

def admin_userprofile(request,id):
    user = Account.objects.get(id=id)
    user_details = Userprofile.objects.get(user=user)
    context = {
        "user":user_details
    }
    return render(request,"admin_panel/admin_userprofile.html",context)
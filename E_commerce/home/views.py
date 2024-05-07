from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

# Create your views here.

def home(request):
    product = Product.objects.all()
    return render(request, 'Home/home.html',{'products':product})
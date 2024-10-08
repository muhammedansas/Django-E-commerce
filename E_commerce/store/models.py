from django.db import models
from products_category.models import catogary
from django.urls import reverse

# Create your models here.  

class Product(models.Model):
    product_name = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/products')
    price = models.IntegerField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    product_category = models.ForeignKey(catogary,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse("product_detail",args=[self.product_category.slug,self.slug])

    def __str__(self):
        return self.product_name
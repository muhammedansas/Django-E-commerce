from django import forms
from store.models import Product

class Product_update_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


    def __init__(self,*args,**kwargs):
        super(Product_update_form,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'    


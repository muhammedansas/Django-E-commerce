from django import forms
from . models import Account,Userprofile
import re
from django.core.exceptions import ValidationError,FieldError
from django.contrib.auth.password_validation import(
    MinimumLengthValidator,
    CommonPasswordValidator,
    NumericPasswordValidator,
)

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
    }))
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']

    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'    



    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match")
            
        
class Userform(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('first_name','last_name','phone_number') 

    def __init__(self,*args,**kwargs):
        super(Userform,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'     

class Userprofileform(forms.ModelForm):
    profile_picture = forms.ImageField(required=False,error_messages={'invalid':("Images files only")},widget=forms.FileInput)
    class Meta:
        model = Userprofile
        fields = ('user','address_first','address_second','profile_picture','city','state','country') 

    def __init__(self,*args,**kwargs):
        super(Userprofileform,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'    

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
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Enter password",
        "class":"form-control",
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder":"Confirm password",
        "class":"form-control",
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"First Name",
        "class":"form-control"
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Last Name",
        "class":'form-control'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder":"Email",
        "class":'form-control'
    }))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={
        "placeholder":"Phoen number",
        "class":'form-control',
    }))
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']


 
    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match")
            
        
class Userform(forms.ModelForm):
    class Meta:
        model = Account
        fields = {'first_name','last_name','phone_number'}   

class Userprofileform(forms.ModelForm):
    profile_picture = forms.ImageField(required=False,error_messages={'invalid':("Images files only")},widget=forms.FileInput)
    class Meta:
        model = Userprofile
        fields = {'address_first','address_second','profile_picture','city','state','country'} 

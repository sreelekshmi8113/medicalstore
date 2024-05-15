from django import forms
from .models import Product
# class LoginForm(forms.Form):
#     email = forms.EmailField(max_length=100,min_length=10)
#     password = forms.CharField(max_length=50,min_length=6)



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','price']
from django import forms
from .models import Product
from django.contrib.auth.models import User
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["name","image","price","description"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password']
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
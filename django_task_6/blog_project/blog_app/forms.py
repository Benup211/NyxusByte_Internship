from django import forms
from django.contrib.auth.models import User
from .models import *
class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username', 'email', 'password']
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ['username', 'password']

class Createblog(forms.ModelForm):
    post_tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.SelectMultiple(attrs={'class': 'form-control'}),to_field_name='id',
        label='tag_user')
    class Meta:
        model=Post
        fields=['title','content','post_tag']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }
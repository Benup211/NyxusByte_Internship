from django import forms
from store.models import *
from django.contrib.auth.models import User
class BookCreationForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
class AuthorCreation(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'
class GenreCreation(forms.ModelForm):
    class Meta:
        model=Genre
        fields='__all__'
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
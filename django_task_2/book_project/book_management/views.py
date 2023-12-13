from django.shortcuts import render
from .models import Book
# Create your views here.
def get_book(request):
    all_books=Book.objects.all()
    return render(request,'book_management/home.html',{'book':all_books})
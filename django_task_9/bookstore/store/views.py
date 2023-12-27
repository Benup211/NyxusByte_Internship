from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import *
# Create your views here.
class HomeView(View):
    def get(self,request):
        books=Book.objects.all()
        return render(request,'store/home.html',{'books':books})
    
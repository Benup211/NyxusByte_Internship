from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from django.views import View
# Create your views here.

class login_view(View):
    def get(self,request):
        return render(request,'userapp/login.html',{'form':LoginForm()})
    
class register_view(View):
    def get(self,request):
        return render(request,'userapp/register.html',{'form':UserRegistrationForm()})

@method_decorator(login_required(login_url="userapp:login"),name="dispatch")
class Homeview(View):
    def get(self,request):
        return render(request,'userapp/home.html')
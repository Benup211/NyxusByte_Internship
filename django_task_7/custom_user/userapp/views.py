from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from django.views import View
from django.contrib.auth import authenticate, login,logout

class login_view(View):
    def get(self,request):
        return render(request,'userapp/login.html',{'form':LoginForm()})
    def post(self,request):
        user_val=LoginForm(request.POST)
        if user_val.is_valid():
            email=user_val.cleaned_data['email']
            password=user_val.cleaned_data['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect("userapp:home")
            else:
                user_val.add_error(None,"Invalid email or password")
        else:
            user_val.add_error(None,"Invalid form")
        return render(request,'userapp/login.html',{'form':user_val})
    
class register_view(View):
    def get(self,request):
        return render(request,'userapp/register.html',{'form':UserRegistrationForm()})
    def post(self,request):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            email_check=form.check_email_exists()
            if email_check:
                check_password=form.clean_confirm_password()
                if check_password:
                    form.save(commit=True)
                    return redirect("userapp:login")
            else:
                form.add_error('email',"Email Already exist")
        return render(request,'userapp/register.html',{'form':form})
@method_decorator(login_required(login_url="userapp:login"),name="dispatch")
class Homeview(View):
    def get(self,request):
        return render(request,'userapp/home.html')

class verify_user(View):
    def get(self,request,user_id):
        try:
            user=User.objects.get(pk=user_id)
            if user:
                user.is_active=True
                user.save()
                return redirect("userapp:login")
        except:
            return redirect("userapp:register")
@method_decorator(login_required(login_url="userapp:login"),name="dispatch")
class logoutView(View):
    def get(self,request):
        logout(request)
        return redirect('userapp:login')
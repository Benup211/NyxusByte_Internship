from django.shortcuts import render,redirect
from django.views import View
from .forms import ProductForm,RegisterForm,LoginForm
from .models import Product
from django.contrib.auth import login,authenticate,logout
class create_product(View):
    def get(self,request):
        product_form=ProductForm()
        context={
            'form':product_form,
            'create':'active'
        }
        return render(request,'product_app/create_product.html',context)
    def post(self, request):
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_app:display')
        else:
            context = {
                'form': form,
                'create':'active'
            }
        return render(request, 'product_app/create_product.html', context)
class product_display(View):
    def get(self,request):
        products=Product.objects.values('id','name')
        context={
            'products':products,
            'display':'active'
        }
        return render(request,'product_app/display_product.html',context)
    
class product_detail(View):
    def get(self,request,id):
        get_product=Product.objects.filter(id=id)
        return render(request,'product_app/detail_product.html',{'product':get_product[0]})

class RegisterUser(View):
    def get(self,request):
        return render(request,'product_app/register.html',{'form':RegisterForm()})
    
    def post(self,request):
        register_val=RegisterForm(request.POST)
        if register_val.is_valid():
            register_val.save()
            return redirect("product_app:login")
        else:
            return render(request,'product_app/register.html',{'form':RegisterForm()})
class LoginView(View):
    def get(self,request):
        return render(request,'product_app/login.html',{'form':LoginForm()})
    def post(self,request):
        login_val=LoginForm(request.POST)
        if login_val.is_valid():
            username=login_val['username']
            password=login_val['password']
            userExist=authenticate(username=username,password=password)
            if userExist is not None:
                login(request,userExist)
            return redirect('product_app:display')
        else:
            return render(request,'product_app/login.html',{'form':RegisterForm()})
class LogoutView(View):
    def get(self,request):
        logout(request.user)
        return redirect('product_app:login')

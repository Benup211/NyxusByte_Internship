from django.shortcuts import render,redirect,get_object_or_404
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
            user=register_val.save(commit=False)
            password=register_val.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect("product_app:login")
        register_val.add_error("Enter field value correctly")
        return render(request,'product_app/register.html',{'form':RegisterForm()})
class LoginView(View):
    def get(self,request):
        return render(request,'product_app/login.html',{'form':LoginForm()})
    def post(self,request):
        login_val=LoginForm(request.POST)
        if login_val.is_valid():
            username=login_val.cleaned_data['username']
            password=login_val.cleaned_data['password']
            userExist=authenticate(username=username,password=password)
            if userExist is not None:
                login(request,userExist)
                return redirect('product_app:display')
            login_val.add_error('username',"Error username or password")
        return render(request,'product_app/login.html',{'form':login_val})
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('product_app:login')
class UpdateProduct(View):
    def get(self,request,id):
        product=get_object_or_404(Product,id=id)
        product_form=ProductForm(instance=product)
        context={
            'form':product_form,
            'pid':id
        }
        return render(request,'product_app/update_product.html',context)
    def post(self,request,id):
        product=get_object_or_404(Product,id=id)
        form=ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_app:detail',id)
        form.add_error('name',"Enter correctly value")
        return render(request,'product_app/update_product.html',{'form':form,'pid':id})
class DeleteProduct(View):
    def post(self,request,id):
        product=get_object_or_404(Product,id=id)
        product.delete()
        return redirect('product_app:display')

        

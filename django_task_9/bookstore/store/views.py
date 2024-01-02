from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='store:login'),name="dispatch")
class HomeView(View):
    def get(self,request):
        genre_id = request.GET.get('genre')
        book_val=request.GET.get('searckBook')
        if genre_id is None and book_val is None:
            books=Book.objects.all()
        elif genre_id is not None:
            books = Book.objects.filter(genre_id=genre_id)
        else:
            books = Book.objects.filter(title__icontains=book_val)
        genre=Genre.objects.all()
        return render(request,'store/home.html',{'books':books,'genre':genre,'messages':''})
    def post(self,request):
        book_id=request.POST.get('book_id')
        try:
            check_cart=Cart.objects.get(user=request.user, items__id=book_id)
            if check_cart is not None:
                check_cart.quantity+=1
                check_cart.save()
                messages='Cart incremented successfully.'
            else:
                new_cart=Cart.objects.create(user=request.user, items_id=book_id)
                new_cart.save()
                messages='New item added to the cart.'
        except:
            new_cart=Cart.objects.create(user=request.user, items_id=book_id)
            new_cart.save()
            messages='New item added to the cart.'
        books=Book.objects.all()
        genre=Genre.objects.all()
        return render(request,'store/home.html',{'books':books,'genre':genre,'messages':messages})
@method_decorator(login_required(login_url='store:login'),name="dispatch")
class CartView(View):
    def get(self,request):
        cart_items=Cart.objects.filter(user=request.user)
        cart_items_dict = {}
        for cart_item in cart_items:
            book_values = {
                "title": cart_item.items.title,  
                "price": cart_item.items.price,
                "book_image": cart_item.items.book_image.url,
                "quantity": cart_item.quantity,
            }
            cart_items_dict[cart_item.id] = book_values
        return render(request,'store/cart.html',{'cart':cart_items_dict})
class LoginView(View):
    def get(self,request):
        return render(request,'login.html',{'form':LoginForm()})
    def post(self,request):
        loginVal=LoginForm(request.POST)
        if loginVal.is_valid():
            username=loginVal.cleaned_data['username']
            password=loginVal.cleaned_data['password']
            getUser=authenticate(username=username,password=password)
            if getUser is not None:
                login(request,getUser)
                return redirect('store:home')
        loginVal.add_error(None,'Error username or password')
        return render(request,'login.html',{'form':loginVal})
class RegisterView(View):
    def get(self,request):
        return render(request,'store/register.html',{'form':RegisterForm})
    def post(self,request):
        register_user=RegisterForm(request.POST)
        if register_user.is_valid():
            register_user.instance.is_active = False
            register_user.save()
            return redirect('store:login')
        return render(request,'store/register.html',{'form':RegisterForm})
@method_decorator(login_required(login_url='store:login'),name="dispatch")
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('store:login')
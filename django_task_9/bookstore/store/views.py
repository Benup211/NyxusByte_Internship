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
        return render(request,'store/home.html',{'books':books,'genre':genre})
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
@method_decorator(login_required(login_url='store:login'),name="dispatch")
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('store:login')
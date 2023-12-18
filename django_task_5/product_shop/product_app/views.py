from django.shortcuts import render,redirect
from django.views import View
from .forms import ProductForm
from .models import Product

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
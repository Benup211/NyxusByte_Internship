from django.shortcuts import render,redirect
from django.views import View
from .forms import ProductForm


class create_product(View):
    def get(self,request):
        product_form=ProductForm()
        context={
            'form':product_form
        }
        return render(request,'product_app/create_product.html',context)
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_app:display')
        else:
            print("Error")
            context = {
                'form': form
            }
        return render(request, 'product_app/create_product.html', context)
class product_display(View):
    def get(self,request):
        return render(request,'product_app/display_product.html')
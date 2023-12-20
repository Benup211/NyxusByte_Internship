from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.views import View
from .forms import *
from .models import *
# Create your views here.
class RegisterUser(View):
    def get(self,request):
        return render(request,'blog_app/register.html',{'form':RegisterForm()})
    
    def post(self,request):
        register_val=RegisterForm(request.POST)
        if register_val.is_valid():
            user=register_val.save(commit=False)
            password=register_val.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect("blog_app:login")
        register_val.add_error("Enter field value correctly")
        return render(request,'blog_app/register.html',{'form':RegisterForm()})
class LoginView(View):
    def get(self,request):
        return render(request,'blog_app/login.html',{'form':LoginForm()})
    def post(self,request):
        login_val=LoginForm(request.POST)
        if login_val.is_valid():
            username=login_val.cleaned_data['username']
            password=login_val.cleaned_data['password']
            userExist=authenticate(username=username,password=password)
            if userExist is not None:
                login(request,userExist)
                return redirect('blog_app:all_blog')
            login_val.add_error('username',"Error username or password")
        return render(request,'blog_app/login.html',{'form':login_val})
class blog_logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("blog_app:login")

class all_blog(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect('blog_app:login')
        else:
            posts = Post.objects.prefetch_related('post_comment', 'post_tag').filter(author=request.user)
            all_post=dict()
            for p in posts:
                all_post[p.id]=p.title
            context={
                "my_blog":"active",
                "all_post":all_post,
            }
            return render(request,'blog_app/post_list.html',context)

class create_post(View):
    def get(self,request,*args,**kwargs):
        return render(request,'blog_app/create_post.html',{'form':Createblog()})
    def post(self,request,*args,**kwargs):
        form=Createblog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog_app:all_blog")
        return render(request,"blog_app/create_post.html",{'form':form})
    
class blog_detail(View):
    def get(self,request,pid,*args,**kwargs):
        context={}
        tag_list=list()
        comments=dict()
        posts=Post.objects.filter(author=request.user).prefetch_related('post_comment', 'post_tag').filter(id=pid)
        for p in posts:
            context={
                'id':p.id,
                'title':p.title,
                'content':p.content,
                'pub_date':p.pub_date
            }
            for t in p.post_tag.all():
                tag_list.append(t.tag_user)
            for c in p.post_comment.all():
                comments[c.comment_user]=c.comment_val
            context["tags"]=tag_list
            context["comment"]=comments
        return render(request,'blog_app/post_detail.html',context)
class DeleteProduct(View):
    def post(self,request,id):
        product=get_object_or_404(Post,id=id)
        product.delete()
        return redirect('blog_app:all_blog')

class other_blog(View):
    def get(self,request):
        posts=Post.objects.exclude(author=request.user.id)
        all_post=dict()
        for p in posts:
                all_post[p.id]=p.title
        context={
                "other_blog":"active",
                "all_post":all_post,
        }
        return render(request,'blog_app/others_blog.html',context)

class other_detail(View):
    def get(self,request,pid,*args,**kwargs):
        context={}
        tag_list=list()
        comments=dict()
        posts=Post.objects.prefetch_related('post_comment', 'post_tag').filter(id=pid)
        for p in posts:
            context={
                'id':p.id,
                'title':p.title,
                'content':p.content,
                'pub_date':p.pub_date
            }
            for t in p.post_tag.all():
                tag_list.append(t.tag_user)
            for c in p.post_comment.all():
                comments[c.comment_user]=c.comment_val
            context["tags"]=tag_list
            context["comment"]=comments
        return render(request,'blog_app/other_detail.html',context)
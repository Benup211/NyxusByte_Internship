from django.shortcuts import render,redirect
from django.views import View
from .models import Post,Tag,Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog_app.forms import LoginForm,Createblog
# Create your views here.
class all_blog(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_anonymous:
            return redirect('blog_app:login')
        else:
            posts = Post.objects.prefetch_related('post_comment', 'post_tag').filter(author=request.user)
            all_post=dict()
            for p in posts:
                all_post[p.id]=p.title
            print(all_post)
            context={
                "my_blog":"active",
                "all_post":all_post,
            }
            return render(request,'blog_app/post_list.html',context)
class blog_login(View):
    def post(self,request,*args,**kwargs):
        context={}
        form=LoginForm(request.POST)
        if form.is_valid()==False:
            form=LoginForm()
            context={
                'error':True
            }
        else:
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            context={
                'error':True,
                "username":username,
                "password":password,
            }
            if user is not None:
                login(request,user)
                return redirect("blog_app:all_blog")
            else:
                context={
                    'error':True
                }
        return render(request,"blog_app/login.html",context)
    def get(self,request,*args,**kwargs):
        return render(request,"blog_app/login.html",{})
class blog_logout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("blog_app:login")
class create_post(View):
    def get(self,request,*args,**kwargs):
        tag_val=Tag.objects.all()
        tag_list=list()
        for t in tag_val:
            tag_list.append(t.tag_user)
        context={
            "create_post":"active",
            "tag_list":tag_list,
        }
        return render(request,'blog_app/create_post.html',context)
    def post(self,request,*args,**kwargs):
        context={}
        form=Createblog(request.POST)
        if form.is_valid()==False:
            form=Createblog()
            context={
                'error':True
            }
        else:
            title=form.cleaned_data['title']
            content=form.cleaned_data['content']
            pub_date=form.cleaned_data['pub_date']
            tag_val=form.cleaned_data['tag']
            tag_user=User.objects.get(username=tag_val)
            new_post = Post.objects.create(title=title, content=content, author=request.user, pub_date=pub_date)
            new_post.post_tag.add(tag_user.id)
            new_post.save()
            return redirect("blog_app:all_blog")
        return render(request,"blog_app/create_post.html",context)

class blog_detail(View):
    def get(self,request,pid,*args,**kwargs):
        context={}
        tag_list=list()
        comments=dict()
        posts=Post.objects.filter(author=request.user).prefetch_related('post_comment', 'post_tag').filter(id=pid)
        for p in posts:
            context={
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
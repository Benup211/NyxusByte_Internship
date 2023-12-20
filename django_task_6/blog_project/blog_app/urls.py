from django.urls import path
from .views import *
app_name="blog_app"
urlpatterns=[
    path('',all_blog.as_view(),name="all_blog"),
    path('login/',LoginView.as_view(),name="login"),
    path('register/',RegisterUser.as_view(),name="register"),
    path('logout/',blog_logout.as_view(),name="logout"),
    path('create/',create_post.as_view(),name="create"),
    path('detail/<int:pid>/',blog_detail.as_view(),name="detail"),
    path('delete/<int:id>/',DeleteProduct.as_view(),name="delete"),
    path('other/',other_blog.as_view(),name="otherblog"),
    path('otherdetail/<int:pid>/',other_detail.as_view(),name="otherdetail"),
]
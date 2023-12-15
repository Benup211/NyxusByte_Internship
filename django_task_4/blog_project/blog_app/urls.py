from django.urls import path
from .views import all_blog,blog_login,blog_logout,create_post,blog_detail
app_name="blog_app"
urlpatterns=[
    path('',all_blog.as_view(),name="all_blog"),
    path('login/',blog_login.as_view(),name="login"),
    path('logout/',blog_logout.as_view(),name="logout"),
    path('create/',create_post.as_view(),name="create"),
    path('detail/<int:pid>',blog_detail.as_view(),name="detail"),
]
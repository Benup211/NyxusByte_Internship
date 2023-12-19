from django.urls import path
from .views import *
app_name="product_app"
urlpatterns=[
    path('',create_product.as_view(),name="create"),
    path('display/',product_display.as_view(),name="display"),
    path('detail/<int:id>/',product_detail.as_view(),name="detail"),
    path('register/',RegisterUser.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('update/<int:id>/',UpdateProduct.as_view(),name="update"),
    path('delete/<int:id>/',DeleteProduct.as_view(),name="delete"),
]
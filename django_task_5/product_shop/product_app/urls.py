from django.urls import path
from .views import create_product,product_display,product_detail
app_name="product_app"
urlpatterns=[
    path('',create_product.as_view(),name="create"),
    path('display/',product_display.as_view(),name="display"),
    path('detail/<int:id>/',product_detail.as_view(),name="detail"),
]
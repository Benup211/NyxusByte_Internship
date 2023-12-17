from django.urls import path
from .views import create_product,product_display
app_name="product_app"
urlpatterns=[
    path('',create_product.as_view(),name="create"),
    path('display/',product_display.as_view(),name="display"),
]
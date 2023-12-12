from django.shortcuts import render
import json
# Create your views here.
def product_view(request):
    json_value=[
        {
            "product_name": "Example Product 1",
            "description": "This is a dummy product for demonstration purposes.",
            "price": 19.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 2",
            "description": "This is another dummy product for demonstration purposes.",
            "price": 29.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 3",
            "description": "Yet another dummy product for demonstration purposes.",
            "price": 39.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 4",
            "description": "A dummy product with a unique description.",
            "price": 49.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 5",
            "description": "A dummy product with a different description.",
            "price": 59.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 6",
            "description": "A dummy product with yet another description.",
            "price": 69.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 7",
            "description": "A dummy product with a creative description.",
            "price": 79.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 8",
            "description": "A dummy product with an interesting description.",
            "price": 89.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 9",
            "description": "A dummy product with a catchy description.",
            "price": 99.99,
            "currency": "USD"
        },
        {
            "product_name": "Example Product 10",
            "description": "A dummy product with a captivating description.",
            "price": 109.99,
            "currency": "USD"
        }
    ]
    return render(request,'product_info/product.html',{'json_val':json_value})
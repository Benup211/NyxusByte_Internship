from django.urls import path
from .views import get_book
urlpatterns=[
    path('home/',get_book,name="get_book"),
]
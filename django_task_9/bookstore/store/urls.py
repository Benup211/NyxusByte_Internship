from django.urls import path
from .views import *
app_name="store"
urlpatterns=[
    path('',HomeView.as_view(),name="home"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
]
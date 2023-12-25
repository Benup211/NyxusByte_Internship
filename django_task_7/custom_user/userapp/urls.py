from django.urls import path
from .views import *
app_name="userapp"
urlpatterns = [
    path('login/', login_view.as_view(), name="login"),
    path('logout/',logoutView.as_view(),name="logout"),
    path('register/', register_view.as_view(), name="register"),
    path('', Homeview.as_view(), name="home"),
    path('verify/<int:user_id>/',verify_user.as_view(),name="verify"),
]
from django.urls import path
from .views import login_view, register_view, Homeview
app_name="userapp"
urlpatterns = [
    path('login/', login_view.as_view(), name="login"),
    path('register/', register_view.as_view(), name="register"),
    path('', Homeview.as_view(), name="home"),
]
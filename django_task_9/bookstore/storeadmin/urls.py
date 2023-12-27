from django.urls import path
from .views import *
app_name="storeadmin"
urlpatterns=[
    path('addbook/',AddBookView.as_view(),name="addbook"),
    path('addauthor/',AddAuthor.as_view(),name="addauthor"),
    path('addgenre/',AddGenre.as_view(),name="addgenre"),
    path('login/',stafflogin.as_view(),name="stafflogin"),
    path('storepanel/',StoreAdminPanel.as_view(),name="storepanel"),
]

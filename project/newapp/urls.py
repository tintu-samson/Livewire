from django.urls import path
from . import views



urlpatterns=[
    path('',views.home,name="home"),
    path('orders',views.orders,name="orders"),
    path('checkout/',views.checkout,name="checkout"), 
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")
]
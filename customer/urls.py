from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from customer.views import marathi,hindi,home

urlpatterns = [
    path('customerclick', views.customerclick_view,name='customerclick'),
    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customerlogin', LoginView.as_view(template_name='insurance/adminlogin.html'),name='customerlogin'),
    path('marathi',marathi.as_view(),name="marathi"),
    path('hindi',hindi.as_view(),name="hindi"),
    path('home',home.as_view(),name="home"),
    
]
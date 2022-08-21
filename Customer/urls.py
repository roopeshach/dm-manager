from django.urls import path
from . import views
urlpatterns = [
    path('login-customer', views.login_customer, name='login-customer'),
    path('customer-home', views.customer_home, name='customer-home'),
    path('logout-customer', views.logout_customer, name='logout-customer'),
]
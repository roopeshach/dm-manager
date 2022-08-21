from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='index'),
    
    path('services', views.ServiceView.as_view(), name="service"),
    path('update-service/<int:pk>', views.UpdateService.as_view(), name="update-service"),
    path('delete-service/<int:id>', views.delete_service, name="delete-service"),

    path('packages', views.PackageView.as_view(), name="package"),
    path('update-package/<int:pk>', views.UpdatePackage.as_view(), name="update-package"),
    path('delete-package/<int:id>', views.delete_package, name="delete-package"),

    path('customers', views.CustomerView.as_view(), name="customer"),
    path('update-customer/<int:pk>', views.UpdateCustomer.as_view(), name="update-customer"),
    path('delete-customer/<int:id>', views.delete_customer, name="delete-customer"),

    path('vendors', views.VendorView.as_view(), name="vendor"),
    path('update-vendor/<int:pk>', views.UpdateVendor.as_view(), name="update-vendor"),
    path('delete-vendor/<int:id>', views.delete_vendor, name="delete-vendor"),

    path('orders', views.OrderView.as_view(), name="order"),
    path('update-order/<int:pk>', views.UpdateOrder.as_view(), name="update-order"),
    path('delete-order/<int:id>', views.delete_order, name="delete-order"),
    


]

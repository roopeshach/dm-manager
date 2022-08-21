from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .forms import  CustomerForm, OrderForm, ServiceForm, PackageForm, VendorForm
from .models import Customer, Service, Package , Vendor, Order

from django.views.generic.edit import UpdateView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin  , UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    if request.user.is_authenticated:

        services = Service.objects.all()
        packages = Package.objects.all()
        customers = Customer.objects.all()
        vendors = Vendor.objects.all()
        orders = Order.objects.all()
        customerwise_orders = []
        for customer in customers:
            customerwise_orders.append({
                'customer':customer,
                'orders':orders.filter(customer=customer).count()
            })
        print(customerwise_orders)
        context = {
            'services': services,
            'packages': packages,
            'customers': customers,
            'vendors': vendors,
            'orders': orders,
            'customerwise_orders': customerwise_orders,
        }
        return render(request, 'Services/index.html', context)
    else:
        return redirect('/login')

#service views
class ServiceView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    def get(self, request):
        form = ServiceForm()
        services = Service.objects.all()
        context = {
            'form': form,
            'services': services
        }
        return render(request, 'Services/services.html', context)

    def post(self, request):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Service added successfully')
            return redirect('/services')
        else:
            messages.add_message(request, messages.INFO, 'Something went wrong')
            return redirect('/services')


class UpdateService(LoginRequiredMixin, UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Service
    fields = ('__all__')

@login_required
def delete_service(request , id):
    service = Service.objects.get(id=id)
    service.delete()
    messages.add_message(request, messages.INFO, 'Service deleted successfully')
    return redirect('/services')

#package views
class PackageView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    def get(self, request):
        form = PackageForm()
        packages = Package.objects.all()
        context = {
            'form': form,
            'packages': packages
        }
        return render(request, 'Services/packages.html', context)

    def post(self, request):
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Package added successfully')
            return redirect('/packages')
        else:
            messages.add_message(request, messages.INFO, 'Something went wrong')
            return redirect('/packages')

class UpdatePackage(LoginRequiredMixin, UpdateView):

    def test_func(self):
        login_url  = 'login/'
        return(self.request.user)
    
    model = Package
    fields = ('__all__')

@login_required
def delete_package(request , id):
    package = Package.objects.get(id=id)
    package.delete()
    messages.add_message(request, messages.INFO, 'Package deleted successfully')
    return redirect('/packages')

#customer views
class CustomerView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    def get(self, request):
        form = CustomerForm()
        customers = Customer.objects.all()
        #get order details for each customer
        for customer in customers:
            customer.orders = Order.objects.filter(customer=customer)
        
        context = {
            'form': form,
            'customers': customers,
        }
        return render(request, 'Services/customers.html', context)



    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Customer added successfully')
            return redirect('/customers')
        else:
            messages.add_message(request, messages.INFO, 'Something went wrong')
            return redirect('/customers')
        
class UpdateCustomer(LoginRequiredMixin, UpdateView):
    
        def test_func(self):
            login_url  = 'login/'
            return(self.request.user)
        
        model = Customer
        fields = ('__all__')

@login_required
def delete_customer(request , id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    messages.add_message(request, messages.INFO, 'Customer deleted successfully')
    return redirect('/customers')

#vendor views
class VendorView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    def get(self, request):
        form = VendorForm()
        vendors = Vendor.objects.all()
        context = {
            'form': form,
            'vendors': vendors
        }
        return render(request, 'Services/vendors.html', context)

    def post(self, request):
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Vendor added successfully')
            return redirect('/vendors')
        else:
            messages.add_message(request, messages.INFO, 'Something went wrong')
            return redirect('/vendors')

class UpdateVendor(LoginRequiredMixin, UpdateView):
        
        def test_func(self):
            login_url  = 'login/'
            return(self.request.user)
        
        model = Vendor
        fields = ('__all__')

@login_required
def delete_vendor(request , id):
    vendor = Vendor.objects.get(id=id)
    vendor.delete()
    messages.add_message(request, messages.INFO, 'Vendor deleted successfully')
    return redirect('/vendors')

#order views
class OrderView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    def test_func(self):
        login_url = 'login/'
        return(self.request.user)

    def get(self, request):
        form = OrderForm()
        orders = Order.objects.all()
        context = {
            'form': form,
            'orders': orders
        }
        return render(request, 'Services/orders.html', context)

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Order added successfully')
            return redirect('/orders')
        else:
            messages.add_message(request, messages.INFO, 'Something went wrong')
            return redirect('/orders')

class UpdateOrder(LoginRequiredMixin, UpdateView):
            
        def test_func(self):
            login_url  = 'login/'
            return(self.request.user)
        
        model = Order
        fields = ('__all__')

@login_required
def delete_order(request , id):
    order = Order.objects.get(id=id)
    order.delete()
    messages.add_message(request, messages.INFO, 'Order deleted successfully')
    return redirect('/orders')



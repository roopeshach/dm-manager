from django.shortcuts import render, redirect

# Create your views here.
from Services.models import Customer, Service, Package , Vendor, Order

from django.views.generic.edit import UpdateView , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin  , UserPassesTestMixin
from django.contrib import messages

def login_customer(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST['password']

        customer = Customer.objects.filter(email=email)
        if customer:
            customer = customer[0]
            if customer.password == password:
                request.session['customer'] = customer.id
                return redirect('customer:customer-home')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid Password')
                return redirect('customer:login-customer')

    return render(request, 'Customer/login_customer.html')

def logout_customer(request):
    request.session.flush()
    return redirect('customer:login-customer')

def customer_home(request):
    if request.session.has_key('customer'):
        orders = Order.objects.filter(customer=request.session['customer'])
        customer = Customer.objects.get(id=request.session['customer'])
        total_paid = 0
        total_amount = 0
        remaining_amount = 0
        for order in orders:
            total_paid += order.paid_amount
            remaining_amount  += (order.total_amount - order.paid_amount)
            total_amount += order.total_amount
        

        context = {
            'orders': orders,
            'customer': customer, 
            'total_paid': total_paid,
            'remaining_amount': remaining_amount,
            'total_amount': total_amount,
        }
        return render(request, 'Customer/home.html', context)
    else:
        return redirect('customer:login-customer')
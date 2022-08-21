from django import forms
from .models import Service, Package, Customer , Vendor, Order

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
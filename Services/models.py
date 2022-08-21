from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:service')
    
class Package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    service = models.ManyToManyField(Service)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('services:package')

class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    address = models.TextField()
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('services:customer')

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.TextField()
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('services:vendor')

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    package = models.ManyToManyField(Package, blank=True, null=True)
    service = models.ManyToManyField(Service, blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse('services:order')
    

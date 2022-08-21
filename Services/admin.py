from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Service)
admin.site.register(Package)
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(Order)

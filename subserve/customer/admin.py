from django.contrib import admin
from .models import Customer
from .models import Manager
# Register your models here.
admin.site.register(Customer)
admin.site.register(Manager)
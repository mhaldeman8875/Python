from django.contrib import admin

# Register your models here.

#This is a register to display on live site
from .models import Product
admin.site.register(Product)
#End
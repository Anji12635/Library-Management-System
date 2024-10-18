from django.contrib import admin

# Register your models here.
from .models import Product,Order
from django.contrib.auth.models import Group

admin.site.site_header = "Library Management System"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('Bookname','category','quantity')
    list_filter = ('category',)
    

admin.site.register(Order)
admin.site.register(Product,ProductAdmin)
#admin.site.unregister(Group)

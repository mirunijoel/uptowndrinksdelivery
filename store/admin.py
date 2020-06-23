from django.contrib import admin
from .models import *

# Register your models here.


# This line changes the type of listing, Filter objects in the Whisky Database
class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Upload a picture for the Product', {'fields': ['picture']}),
        ('Enter the Name of the Product', {'fields': ['product_type']}),
        ('Enter the Name of the Product', {'fields': ['name']}),
        ('Enter the Capacity of the Product (Mililitre or Litre)', {'fields': ['capacity']}),
        ('Enter the Price of the Product (Ensure to place a comma and a space in thousands)', {'fields': ['cash']}),
        ('Enter the Date when the Product is Uploaded (Enter Date)', {'fields': ['date_uploaded']}),
        ('Does the Product Require Shipping', {'fields': ['digital']}),
    ]
    list_display = ('name', 'capacity', 'cash', 'cash', 'picture', 'digital')
    list_filter = ['name', 'capacity', 'date_uploaded']


admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)


class ShippingAddressAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name of the Customer', {'fields': ['customer']}),
        ('Order taken', {'fields': ['order']}),
        ('Address of the Customer', {'fields': ['address']}),
        ('Phone number of the Customer', {'fields': ['phone']}),
        ('City of the Customer', {'fields': ['city']}),
        # ('Date added', {'fields': ['date_added']}),
    ]
    list_display = ('customer', 'phone', 'order', 'address', 'city', 'date_added')
    list_filter = ['customer', 'order', 'address', 'date_added']


admin.site.register(ShippingAddress, ShippingAddressAdmin)

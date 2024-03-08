from django.contrib import admin

from .models import TShirt, Order, Customer

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'email', 'product', 'town_city', 'postcode')
    list_filter = ['email']

class TShirtAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'colour', 'size', 'price')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'total_orders')

# List of admin views registered
admin.site.register(Customer, CustomerAdmin)
admin.site.register(TShirt, TShirtAdmin)
admin.site.register(Order, OrderAdmin)




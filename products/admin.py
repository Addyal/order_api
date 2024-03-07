from django.contrib import admin

from .models import TShirt, Order, Customer

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'product', 'town_city', 'postcode')

# List of admin views registered
admin.site.register(Customer)
admin.site.register(TShirt)
admin.site.register(Order, OrderAdmin)




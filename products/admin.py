from django.contrib import admin

from .models import TShirt, Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'name', 'email', 'product', 'town_city', 'postcode')
    list_filter = ['email']

# List of admin views registered
admin.site.register(TShirt)
admin.site.register(Order, OrderAdmin)




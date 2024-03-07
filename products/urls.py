from django.urls import path

from . import views
from .views import tshirt_list, order_page, order_confirmation, latest_orders

# list of URL patterns
urlpatterns = [
    path("", views.index, name="index"),
    path('tshirts/', tshirt_list, name='tshirt_list'),
    path('tshirts/<int:tshirt_id>/order/', order_page, name='order_page'),
    path('order_confirmation/<str:order_number>/', order_confirmation, name='order_confirmation'),
    path('latest_orders/', latest_orders, name='latest_orders'),
]
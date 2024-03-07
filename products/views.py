#django imports
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import OrderForm
from .models import TShirt, Order, Customer

#Default index/homepage
def index(request):
    return HttpResponse("Home page")

# return a list of tshirts
def tshirt_list(request):
    tshirts = TShirt.objects.all()
    return render(request, 'tshirt_list.html', {'tshirts': tshirts})

# View to show the page after the user has pressed 'order now'. This allows them to give there information 
def order_page(request, tshirt_id):
    tshirt = TShirt.objects.get(pk=tshirt_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = tshirt
            order.save()
            return redirect('order_confirmation', order_number=order.order_number)
    else:
        form = OrderForm()

    return render(request, 'order_page.html', {'tshirt': tshirt, 'form': form})

# View to show the order confirmation page, simply prints out the uuid that has been made and says thanks
def order_confirmation(request, order_number):
    order = Order.objects.get(order_number=order_number)
    return render(request, 'order_confirmation.html', {'order': order})

# Last 50 orders to be shown, this would be for the back office
def latest_orders(request):
    # Fetch the latest 50 orders with related TShirt
    latest_orders = Order.objects.order_by('-id')[:50].select_related('product')  
    # Access the object of the Customer model
    customer_objs = Customer.objects.all()
    j = customer_objs.get(email="test@test.com").total_orders
    print('CUSTOMER OBJECTS HERE')
    print(j)
    return render(request, 'latest_orders.html', {'latest_orders': latest_orders, 'customer_objs': customer_objs})

#imports
from django.db import models
import uuid

# Customer master list, for now we only need to store email and total number of orders associated with this email account
class Customer(models.Model):
    email = models.EmailField(unique=True)
    total_orders = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.email


# tshirt model, allow for a list of tshirts and their details
class TShirt(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="tshirts", blank=True, null=True)
    colour = models.CharField(max_length=10, blank='See Image')
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

# Order model, allows us to put in the information provided by the user 
class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    product = models.ForeignKey(TShirt, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    town_city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = str(uuid.uuid4()).split('-')[0].upper()

        # Update total_orders in the Customer model
        customer, created = Customer.objects.get_or_create(email=self.email)

        # Increment the total number of orders that the customer has made
        customer.total_orders += 1
        customer.save()

        super().save(*args, **kwargs)
#imports
from django.db import models
import uuid

class TShirt(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="tshirts", blank=True, null=True)
    size = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

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
        super().save(*args, **kwargs)

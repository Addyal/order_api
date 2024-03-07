# for generating 50 fake orders

# TEST
# This didn't work - ended up doing manually as deemed wasn't required
# Will return 


exit() 

import random
from faker import Faker 
from models import Order, TShirt 


def create_random_orders(num_orders=50):
    fake = Faker()

    # Get all T-shirts from the database
    tshirts = TShirt.objects.all()

    for _ in range(num_orders):
        # Generate random order details
        order_number = fake.uuid4().split('-')[0].upper()
        tshirt = random.choice(tshirts)
        name = fake.name()
        email = fake.email()
        address1 = fake.street_address()
        address2 = fake.secondary_address()
        town_city = fake.city()
        postcode = fake.postcode()

        # Create and save the order
        Order.objects.create(
            order_number=order_number,
            product=tshirt,
            name=name,
            email=email,
            address1=address1,
            address2=address2,
            town_city=town_city,
            postcode=postcode
        )

if __name__ == "__main__":
    create_random_orders()

# Generated by Django 5.0.3 on 2024-03-08 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]

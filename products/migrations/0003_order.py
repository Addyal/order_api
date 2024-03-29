# Generated by Django 5.0.3 on 2024-03-07 08:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_tshirt_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address1', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255)),
                ('town_city', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.tshirt')),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-07 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
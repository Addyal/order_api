# Generated by Django 5.0.3 on 2024-03-08 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_customer_id_alter_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirt',
            name='product_id',
            field=models.CharField(max_length=20, verbose_name=models.AutoField(primary_key=True)),
        ),
    ]

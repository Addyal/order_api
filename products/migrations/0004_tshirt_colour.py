# Generated by Django 5.0.3 on 2024-03-07 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='colour',
            field=models.CharField(blank='See Image', max_length=10),
        ),
    ]

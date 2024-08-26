# Generated by Django 5.0.7 on 2024-08-26 07:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
        ('orders', '0011_remove_orderdetails_ordered_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='ordered_food_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='carts.cartitem'),
        ),
    ]

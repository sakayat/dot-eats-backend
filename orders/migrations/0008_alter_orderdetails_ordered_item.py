# Generated by Django 5.0.7 on 2024-08-26 07:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_alter_orderdetails_ordered_item'),
        ('restaurant', '0015_rename_tag_foodtag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='ordered_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.fooditem'),
        ),
    ]

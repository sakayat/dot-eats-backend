# Generated by Django 5.0.7 on 2024-08-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0010_fooditem_name_slug_alter_fooditem_restaurant_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
                ('tag_slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='tags',
            field=models.ManyToManyField(to='restaurant.foodtags'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shoe_items", "0007_remove_sales_stats_brand_ordered"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

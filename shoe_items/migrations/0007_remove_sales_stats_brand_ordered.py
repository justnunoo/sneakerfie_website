# Generated by Django 5.0.3 on 2024-03-25 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shoe_items", "0006_alter_product_brands_delete_brands"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sales_stats",
            name="brand_ordered",
        ),
    ]

# Generated by Django 5.0.1 on 2024-03-17 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_inventory_prediction_inventory_review_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.category'),
        ),
    ]

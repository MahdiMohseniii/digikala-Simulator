# Generated by Django 5.0.7 on 2024-08-07 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_alter_order_date_alter_product_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 7, 20, 13, 17, 257928)),
        ),
    ]

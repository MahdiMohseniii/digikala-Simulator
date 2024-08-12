# Generated by Django 5.0.7 on 2024-08-06 15:33

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_is_sale_product_sale_price_alter_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MaxValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 6, 19, 3, 51, 942819)),
        ),
    ]

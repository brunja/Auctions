# Generated by Django 3.1.7 on 2021-04-08 07:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0018_auto_20210405_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='amount',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.01)]),
        ),
    ]

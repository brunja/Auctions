# Generated by Django 3.1.7 on 2021-03-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auto_20210322_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='item',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(related_name='watchlist_items', to='auction.Item'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-24 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20210324_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='item',
            field=models.ManyToManyField(blank=True, related_name='watchlist_items', to='auction.Item'),
        ),
    ]

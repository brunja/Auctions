# Generated by Django 3.1.7 on 2021-04-04 17:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0016_auto_20210326_0927'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='watchers',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='WatchList',
        ),
    ]

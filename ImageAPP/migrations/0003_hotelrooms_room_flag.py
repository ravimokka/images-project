# Generated by Django 2.1.7 on 2019-04-27 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageAPP', '0002_auto_20190427_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelrooms',
            name='room_flag',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

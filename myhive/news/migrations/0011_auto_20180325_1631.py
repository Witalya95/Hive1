# Generated by Django 2.0.2 on 2018-03-25 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20180324_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 3, 25, 16, 31, 23, 717570), verbose_name='Публікація'),
        ),
    ]

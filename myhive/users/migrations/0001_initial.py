# Generated by Django 2.0.2 on 2018-04-24 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_phone', models.CharField(blank=True, default='', max_length=12, verbose_name='Номер мобільного')),
                ('city', models.CharField(blank=True, default='', max_length=30, verbose_name='Місто')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Користувач',
            },
        ),
    ]
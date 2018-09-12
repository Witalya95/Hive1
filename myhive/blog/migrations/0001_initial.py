# Generated by Django 2.0.2 on 2018-03-19 18:32

import datetime
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
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Короткий опис')),
                ('content', models.TextField(verbose_name='Повний опис')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2018, 3, 19, 20, 32, 47, 88097), verbose_name='Дата публікації')),
                ('is_commentable', models.BooleanField(default=True, verbose_name='Можливість коментування')),
                ('user', models.ForeignKey(default='admin', editable=False, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted'],
                'verbose_name': 'Стаття',
                'verbose_name_plural': 'Статті',
            },
        ),
    ]
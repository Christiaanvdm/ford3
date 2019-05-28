# Generated by Django 2.1.7 on 2019-05-27 14:31

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvinceUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('ford3.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='account_activated',
            field=models.BooleanField(default=False),
        ),
    ]

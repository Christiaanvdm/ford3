# Generated by Django 2.1.7 on 2019-05-14 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0042_auto_20190514_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='deleted',
            field=models.BooleanField(default=False, help_text='Qualification has been deleted'),
        ),
    ]

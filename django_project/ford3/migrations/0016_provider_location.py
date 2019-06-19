# Generated by Django 2.2 on 2019-06-19 09:29

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0015_auto_20190617_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, help_text="The spatial point of the provider's head office", null=True, srid=4326),
        ),
    ]

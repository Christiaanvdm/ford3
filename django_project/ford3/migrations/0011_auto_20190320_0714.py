# Generated by Django 2.1.7 on 2019-03-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0010_remove_qualification_qualification_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='require_aps_score',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='requirement',
            name='require_certain_subjects',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

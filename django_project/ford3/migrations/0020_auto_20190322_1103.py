# Generated by Django 2.1.7 on 2019-03-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0019_qualificationevent_other_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualificationentrancerequirementsubject',
            name='minimum_score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.1.9 on 2019-07-20 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0025_remove_requirement_admission_point_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='is_language',
            field=models.BooleanField(blank=True, default=False, help_text='Is the subject a language?', null=True),
        ),
    ]

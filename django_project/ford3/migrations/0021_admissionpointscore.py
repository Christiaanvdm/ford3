# Generated by Django 2.1.9 on 2019-07-19 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0020_peoplegroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionPointScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, help_text='The admission point score required for the qualification', null=True)),
                ('people_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.PeopleGroup')),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ford3.Requirement')),
            ],
        ),
    ]

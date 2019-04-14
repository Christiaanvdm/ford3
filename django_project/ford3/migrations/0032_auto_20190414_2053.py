# Generated by Django 2.1.7 on 2019-04-14 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ford3', '0031_merge_20190328_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provider',
            old_name='postal_address',
            new_name='physical_postal_code',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='provider',
            name='postal_address_city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='postal_address_differs',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='postal_address_line_1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='postal_address_line_2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='provider',
            name='postal_postal_code',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
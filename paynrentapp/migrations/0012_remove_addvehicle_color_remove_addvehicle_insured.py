# Generated by Django 4.1.6 on 2023-05-22 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0011_addvehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addvehicle',
            name='color',
        ),
        migrations.RemoveField(
            model_name='addvehicle',
            name='insured',
        ),
    ]
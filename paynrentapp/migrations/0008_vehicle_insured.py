# Generated by Django 4.1.6 on 2023-03-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0007_rename_modedlyear_vehicle_modelyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='insured',
            field=models.CharField(default='', max_length=70),
        ),
    ]

# Generated by Django 4.1.6 on 2023-03-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=150)),
                ('icon', models.ImageField(upload_to='static/')),
            ],
        ),
    ]

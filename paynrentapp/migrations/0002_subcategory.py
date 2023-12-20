# Generated by Django 4.1.6 on 2023-03-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategoryname', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=150)),
                ('icon', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
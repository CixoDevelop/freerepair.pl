# Generated by Django 4.0 on 2021-12-12 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinboard', '0002_pin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pin',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pin',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
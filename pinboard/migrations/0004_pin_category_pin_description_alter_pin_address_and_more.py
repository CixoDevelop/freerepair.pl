# Generated by Django 4.0 on 2021-12-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinboard', '0003_alter_pin_email_alter_pin_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='category',
            field=models.CharField(choices=[('A', 'Naprawa komputerów / laptopów'), ('B', 'Naprawa sprzętu audio'), ('C', 'Naprawa smartfonów / tabletów'), ('D', 'Naprawa sprzętu retro'), ('E', 'Odnawianie sprawnego sprzętu retro'), ('F', 'Odnawianie sprawnego sprzętu'), ('G', 'Naprawa drobnej elektroniki'), ('H', 'Elektronik - wszystkonaprawiający'), ('I', 'Serwisant - wszstkonaprawiający')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='pin',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='pin',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pin',
            name='facebook',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pin',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='pin',
            name='status',
            field=models.CharField(choices=[('A', 'Aktualnie nie przyjmuję zleceń'), ('B', 'Gotowy do przyjęcia zleceń')], default='B', max_length=1),
        ),
    ]

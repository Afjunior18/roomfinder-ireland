# Generated by Django 3.2 on 2024-02-27 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_room_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 3.2 on 2024-03-04 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_remove_room_room_photos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['price']},
        ),
    ]
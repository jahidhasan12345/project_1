# Generated by Django 4.2 on 2023-04-11 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0003_rename_kitab_book'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='kitab',
        ),
    ]

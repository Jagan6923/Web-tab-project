# Generated by Django 5.0.2 on 2024-02-11 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_project_delete_field_delete_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='project',
            new_name='Patient',
        ),
    ]

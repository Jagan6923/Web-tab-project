# Generated by Django 4.2.5 on 2024-02-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0010_alter_draggableinput_input_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draggableinput',
            name='input_id',
            field=models.IntegerField(),
        ),
    ]

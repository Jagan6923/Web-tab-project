# Generated by Django 4.2.5 on 2024-02-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0008_alter_draggableinput_x_axis_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='draggableinput',
            name='input_id',
            field=models.IntegerField(default=0),
        ),
    ]

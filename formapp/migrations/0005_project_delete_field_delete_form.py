# Generated by Django 5.0.2 on 2024-02-11 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0004_field_form_delete_patient_field_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Field',
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]

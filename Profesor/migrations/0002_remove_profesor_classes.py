# Generated by Django 5.0.6 on 2024-07-04 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profesor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='classes',
        ),
    ]

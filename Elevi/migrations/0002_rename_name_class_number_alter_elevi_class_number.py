# Generated by Django 5.0.6 on 2024-07-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elevi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='name',
            new_name='number',
        ),
        migrations.AlterField(
            model_name='elevi',
            name='class_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
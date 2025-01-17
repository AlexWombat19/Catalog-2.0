# Generated by Django 5.0.6 on 2024-07-08 14:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Elevi', '0002_rename_name_class_number_alter_elevi_class_number'),
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.RenameField(
            model_name='elevi',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='elevi',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='elevi',
            name='user',
        ),
        migrations.AlterField(
            model_name='elevi',
            name='class_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.class'),
        ),
    ]

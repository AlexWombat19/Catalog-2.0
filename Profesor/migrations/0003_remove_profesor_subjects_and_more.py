# Generated by Django 5.0.6 on 2024-07-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profesor', '0002_remove_profesor_classes'),
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesor',
            name='subjects',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='last_name',
        ),
        migrations.AddField(
            model_name='profesor',
            name='class_numbers',
            field=models.ManyToManyField(blank=True, to='administrator.class'),
        ),
        migrations.AddField(
            model_name='profesor',
            name='subject',
            field=models.CharField(choices=[('mathematics', 'Mathematics'), ('chemistry', 'Chemistry'), ('history', 'History')], default='Unknown', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]

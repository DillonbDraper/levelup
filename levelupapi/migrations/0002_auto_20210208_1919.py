# Generated by Django 3.1.6 on 2021-02-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='scheduler',
            new_name='organizer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_time',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default='2021-02-04'),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default='12:00'),
        ),
    ]